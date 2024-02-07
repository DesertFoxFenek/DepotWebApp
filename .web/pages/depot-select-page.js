/** @jsxImportSource @emotion/react */


import { Fragment, useCallback, useContext } from "react"
import { Button_5cbb2952409d1e5ed6e42602daa56ec7, Fragment_fd0e7cb8f9fb4669a6805377d925fba0 } from "/utils/stateful_components"
import { Button, Center, Heading, option, Select, VStack } from "@chakra-ui/react"
import { EventLoopContext, StateContexts } from "/utils/context"
import "@radix-ui/themes/styles.css"
import "focus-visible/dist/focus-visible"
import { Event } from "/utils/state"
import { Theme as RadixThemesTheme } from "@radix-ui/themes"
import theme from "/utils/theme.js"
import NextHead from "next/head"



export function Heading_c41acc6487a3a197def89d41372971c3 () {
  const state__select_state = useContext(StateContexts.state__select_state)


  return (
    <Heading>
  {state__select_state.option}
</Heading>
  )
}

export function Button_f7ff595449f217189aced14722bcf7e4 () {
  const state__select_state = useContext(StateContexts.state__select_state)
  const [addEvents, connectError] = useContext(EventLoopContext);

  const on_click_05a1454f098d44e2d161971ba105249d = useCallback((_e) => addEvents([Event("state.select_state.go_to_mng", {option:state__select_state.option})], (_e), {}), [addEvents, Event, state__select_state])

  return (
    <Button onClick={on_click_05a1454f098d44e2d161971ba105249d}>
  {`Potwierdz`}
</Button>
  )
}

export function Select_8de14e86e42a04a0bf398feeae29535a () {
  const state__select_state = useContext(StateContexts.state__select_state)
  const [addEvents, connectError] = useContext(EventLoopContext);

  const on_change_1278fdcf53f69fffb9885347b6dd9dba = useCallback((_e0) => addEvents([Event("state.select_state.set_option", {value:_e0.target.value})], (_e0), {}), [addEvents, Event])

  return (
    <Select onChange={on_change_1278fdcf53f69fffb9885347b6dd9dba} sx={{"width": "50", "height": "10", "margin": "auto"}}>
  {state__select_state.options.map((item, index_05754def86711a0e82b997b1b77b3df2) => (
  <option key={index_05754def86711a0e82b997b1b77b3df2} value={item}>
  {item}
</option>
))}
</Select>
  )
}

export default function Component() {

  return (
    <Fragment>
  <Fragment_fd0e7cb8f9fb4669a6805377d925fba0/>
  <Fragment>
  <Button_5cbb2952409d1e5ed6e42602daa56ec7/>
  <VStack spacing={`1.5em`} sx={{"fontSize": "2em", "paddingTop": "10%"}}>
  <Heading_c41acc6487a3a197def89d41372971c3/>
  <Center>
  <Select_8de14e86e42a04a0bf398feeae29535a/>
</Center>
  <Button_f7ff595449f217189aced14722bcf7e4/>
</VStack>
</Fragment>
  <NextHead>
  <title>
  {`Depot Selection`}
</title>
  <meta content={`A Reflex app.`} name={`description`}/>
  <meta content={`favicon.ico`} property={`og:image`}/>
</NextHead>
</Fragment>
  )
}
