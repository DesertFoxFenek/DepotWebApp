import { createContext, useContext, useMemo, useReducer, useState } from "react"
import { applyDelta, Event, hydrateClientStorage, useEventLoop, refs } from "/utils/state.js"

export const initialState = {"state": {"is_hydrated": false, "router": {"session": {"client_token": "", "client_ip": "", "session_id": ""}, "headers": {"host": "", "origin": "", "upgrade": "", "connection": "", "pragma": "", "cache_control": "", "user_agent": "", "sec_websocket_version": "", "sec_websocket_key": "", "sec_websocket_extensions": "", "accept_encoding": "", "accept_language": ""}, "page": {"host": "", "path": "", "raw_path": "", "full_path": "", "full_raw_path": "", "params": {}}}}, "state.login_state": {"depots": [], "login": "", "output": "", "password": ""}, "state.input_state_login": {"text_login": "Login", "text_password": "Hasło"}, "state.manager_data": {"free_vehicles": [], "vehicle_timetable": []}, "state.select_state": {"depot": [], "option": "Wybierz pozycje", "options": ["Zajezdnia Borek", "Zajezdnia Olbin", "Zajezdnia Gaj", "Zajezdnia Obornicka"]}}

export const ColorModeContext = createContext(null);
export const UploadFilesContext = createContext(null);
export const DispatchContext = createContext(null);
export const StateContexts = {
  state: createContext(null),
  state__login_state: createContext(null),
  state__input_state_login: createContext(null),
  state__manager_data: createContext(null),
  state__select_state: createContext(null),
}
export const EventLoopContext = createContext(null);
export const clientStorage = {"cookies": {}, "local_storage": {}}

export const onLoadInternalEvent = () => [Event('state.on_load_internal')]

export const initialEvents = () => [
    Event('state.hydrate', hydrateClientStorage(clientStorage)),
    ...onLoadInternalEvent()
]

export const isDevMode = true

export function UploadFilesProvider({ children }) {
  const [filesById, setFilesById] = useState({})
  refs["__clear_selected_files"] = (id) => setFilesById(filesById => {
    const newFilesById = {...filesById}
    delete newFilesById[id]
    return newFilesById
  })
  return (
    <UploadFilesContext.Provider value={[filesById, setFilesById]}>
      {children}
    </UploadFilesContext.Provider>
  )
}

export function EventLoopProvider({ children }) {
  const dispatch = useContext(DispatchContext)
  const [addEvents, connectError] = useEventLoop(
    dispatch,
    initialEvents,
    clientStorage,
  )
  return (
    <EventLoopContext.Provider value={[addEvents, connectError]}>
      {children}
    </EventLoopContext.Provider>
  )
}

export function StateProvider({ children }) {
  const [state, dispatch_state] = useReducer(applyDelta, initialState["state"])
  const [state__login_state, dispatch_state__login_state] = useReducer(applyDelta, initialState["state.login_state"])
  const [state__input_state_login, dispatch_state__input_state_login] = useReducer(applyDelta, initialState["state.input_state_login"])
  const [state__manager_data, dispatch_state__manager_data] = useReducer(applyDelta, initialState["state.manager_data"])
  const [state__select_state, dispatch_state__select_state] = useReducer(applyDelta, initialState["state.select_state"])
  const dispatchers = useMemo(() => {
    return {
      "state": dispatch_state,
      "state.login_state": dispatch_state__login_state,
      "state.input_state_login": dispatch_state__input_state_login,
      "state.manager_data": dispatch_state__manager_data,
      "state.select_state": dispatch_state__select_state,
    }
  }, [])

  return (
    <StateContexts.state.Provider value={ state }>
    <StateContexts.state__login_state.Provider value={ state__login_state }>
    <StateContexts.state__input_state_login.Provider value={ state__input_state_login }>
    <StateContexts.state__manager_data.Provider value={ state__manager_data }>
    <StateContexts.state__select_state.Provider value={ state__select_state }>
      <DispatchContext.Provider value={dispatchers}>
        {children}
      </DispatchContext.Provider>
    </StateContexts.state__select_state.Provider>
    </StateContexts.state__manager_data.Provider>
    </StateContexts.state__input_state_login.Provider>
    </StateContexts.state__login_state.Provider>
    </StateContexts.state.Provider>
  )
}