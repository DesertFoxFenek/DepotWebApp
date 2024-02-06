/** @jsxImportSource @emotion/react */


import { Fragment, useCallback, useContext } from "react"
import { Button_5cbb2952409d1e5ed6e42602daa56ec7, Fragment_fd0e7cb8f9fb4669a6805377d925fba0 } from "/utils/stateful_components"
import { Button, Heading, Input, VStack } from "@chakra-ui/react"
import "focus-visible/dist/focus-visible"
import { EventLoopContext } from "/utils/context"
import { Event, set_val } from "/utils/state"
import NextHead from "next/head"



export function Input_e1c0ce5e4ccf50e17bbac95aa1d7aee3 () {
  const [addEvents, connectError] = useContext(EventLoopContext);

  const on_blur_a85fcdf8771ae6a4010cde8adb35d12d = useCallback((_e0) => addEvents([Event("state.login_state.set_password", {value:_e0.target.value})], (_e0), {}), [addEvents, Event])

  return (
    <Input onBlur={on_blur_a85fcdf8771ae6a4010cde8adb35d12d} placeholder={`Hasło`} sx={{"width": "50", "height": "10"}} type={`password`}/>
  )
}

export function Input_a7b6ef1dbc2ec16742e76bfe5d13a654 () {
  const [addEvents, connectError] = useContext(EventLoopContext);

  const on_blur_b0df2f276509ef0acec4641b5ed2c4a1 = useCallback((_e0) => addEvents([Event("state.login_state.set_login", {value:_e0.target.value})], (_e0), {}), [addEvents, Event])

  return (
    <Input onBlur={on_blur_b0df2f276509ef0acec4641b5ed2c4a1} placeholder={`Login`} sx={{"width": "50", "height": "10"}} type={`text`}/>
  )
}

export function Button_aadf83ce1311ca3979c6879725f578a0 () {
  const [addEvents, connectError] = useContext(EventLoopContext);

  const on_click_25489bb2945b35a89473bc055bd75200 = useCallback((_e) => addEvents([Event("state.login_state.get_auth", {})], (_e), {}), [addEvents, Event])

  return (
    <Button onClick={on_click_25489bb2945b35a89473bc055bd75200}>
  {`Zaloguj`}
</Button>
  )
}

export default function Component() {

  return (
    <Fragment>
  <Fragment_fd0e7cb8f9fb4669a6805377d925fba0/>
  <Fragment>
  <Button_5cbb2952409d1e5ed6e42602daa56ec7/>
  <VStack spacing={`1.5em`} sx={{"fontSize": "2em", "paddingTop": "10%"}}>
  <Heading sx={{"fontSize": "2em"}}>
  {`Witaj. Proszę zaloguj się i wybierz zajezdnie.`}
</Heading>
  <Input_a7b6ef1dbc2ec16742e76bfe5d13a654/>
  <Input_e1c0ce5e4ccf50e17bbac95aa1d7aee3/>
  <Button_aadf83ce1311ca3979c6879725f578a0/>
</VStack>
</Fragment>
  <NextHead>
  <title>
  {`DepotWebApp`}
</title>
  <meta content={`A Reflex app.`} name={`description`}/>
  <meta content={`favicon.ico`} property={`og:image`}/>
</NextHead>
</Fragment>
  )
}
