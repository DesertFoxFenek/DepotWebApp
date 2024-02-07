/** @jsxImportSource @emotion/react */


import { Fragment, useCallback, useContext } from "react"
import { Button_5cbb2952409d1e5ed6e42602daa56ec7, Fragment_fd0e7cb8f9fb4669a6805377d925fba0 } from "/utils/stateful_components"
import { AlertDialog, AlertDialogBody, AlertDialogContent, AlertDialogFooter, AlertDialogHeader, AlertDialogOverlay, Box, Button, Heading, Image as ChakraImage, Link, Spacer, Text, VStack } from "@chakra-ui/react"
import "focus-visible/dist/focus-visible"
import "gridjs/dist/theme/mermaid.css"
import { Grid as DataTableGrid } from "gridjs-react"
import { EventLoopContext, StateContexts } from "/utils/context"
import { Event } from "/utils/state"
import NextLink from "next/link"
import NextHead from "next/head"



export function Text_2bb435c98cbb85d29f68337cd327b186 () {
  const state__sidebar_state = useContext(StateContexts.state__sidebar_state)


  return (
    <Text>
  {state__sidebar_state.brigades_num}
</Text>
  )
}

export function Button_ada31a03f76209a573d1a66423fa4bed () {
  const [addEvents, connectError] = useContext(EventLoopContext);

  const on_click_0922f10ec3b2f1bc33ad0184ca94cc10 = useCallback((_e) => addEvents([Event("state.alert_dialog_state.change", {})], (_e), {}), [addEvents, Event])

  return (
    <Button onClick={on_click_0922f10ec3b2f1bc33ad0184ca94cc10} sx={{"bottom": "70px", "position": "fixed"}}>
  {`O stronie`}
</Button>
  )
}

export function Button_87a012435755203bce2f4d92b11c7acf () {
  const [addEvents, connectError] = useContext(EventLoopContext);

  const on_click_05ec907548497d5db8aff4f24661803b = useCallback((_e) => addEvents([Event("state.login_state.log_out", {})], (_e), {}), [addEvents, Event])

  return (
    <Button onClick={on_click_05ec907548497d5db8aff4f24661803b} sx={{"bottom": "20px", "position": "fixed"}}>
  {`Wyloguj`}
</Button>
  )
}

export function Text_0e668654e2c4c07b29717671d68b67d0 () {
  const state__sidebar_state = useContext(StateContexts.state__sidebar_state)


  return (
    <Text>
  {state__sidebar_state.depot_adress}
</Text>
  )
}

export function Grid_877aaff9bcb56b5c7ab5a50dfebbfc00 () {
  const state__data_table_state = useContext(StateContexts.state__data_table_state)


  return (
    <DataTableGrid columns={state__data_table_state.columns} css={{"smoothScrollY": true}} data={state__data_table_state.data} pagination={true} resizable={true} search={true}/>
  )
}

export function Alertdialog_c96281feaf3b7cbd9261d92fb8b998ee () {
  const state__alert_dialog_state = useContext(StateContexts.state__alert_dialog_state)


  return (
    <AlertDialog isOpen={state__alert_dialog_state.show}>
  <AlertDialogOverlay>
  <AlertDialogContent>
  <AlertDialogHeader>
  {`O stronie`}
</AlertDialogHeader>
  <AlertDialogBody>
  {`Strona stworzona przy wykorzystaniu biblioteki reflex połączoną z bazą danych w serwise Azure. Stan pojazdów/linii/brygad/czasów i innych wartości nie pokrywa się z realnymi. Dane z grudnia 2023 roku.`}
</AlertDialogBody>
  <AlertDialogBody>
  {`Projekt jest wariancją rozwojową konsolowej wersji utworzonej na potrzeby zajęć. `}
  <Link as={NextLink} href={`https://github.com/DesertFoxFenek/DepotApp`} isExternal={true} sx={{"color": "rgb(107,99,246)"}}>
  {`Wersja konsolowa`}
</Link>
</AlertDialogBody>
  <AlertDialogBody>
  {`Autor: `}
  <Link as={NextLink} href={`https://github.com/DesertFoxFenek`} isExternal={true} sx={{"color": "rgb(107,99,246)"}}>
  {`Desert_Fox_Fenek`}
</Link>
</AlertDialogBody>
  <AlertDialogBody>
  {`Wersja: 0.2.24.02WE`}
</AlertDialogBody>
  <AlertDialogFooter>
  <Button_cc0cda26b8d2cad6ca4c35a66fba8941/>
</AlertDialogFooter>
</AlertDialogContent>
</AlertDialogOverlay>
</AlertDialog>
  )
}

export function Button_cc0cda26b8d2cad6ca4c35a66fba8941 () {
  const [addEvents, connectError] = useContext(EventLoopContext);

  const on_click_0922f10ec3b2f1bc33ad0184ca94cc10 = useCallback((_e) => addEvents([Event("state.alert_dialog_state.change", {})], (_e), {}), [addEvents, Event])

  return (
    <Button onClick={on_click_0922f10ec3b2f1bc33ad0184ca94cc10}>
  {`Zamknij`}
</Button>
  )
}

export function Text_18e2858f3f113be24440dab569919fe6 () {
  const state__sidebar_state = useContext(StateContexts.state__sidebar_state)


  return (
    <Text>
  {state__sidebar_state.vehicles_num}
</Text>
  )
}

export function Heading_73213fd57920090aa2f067d6bb5028aa () {
  const state__sidebar_state = useContext(StateContexts.state__sidebar_state)


  return (
    <Heading sx={{"textAlign": "center", "marginBottom": "1em"}}>
  {state__sidebar_state.depot_name}
</Heading>
  )
}

export default function Component() {

  return (
    <Fragment>
  <Fragment_fd0e7cb8f9fb4669a6805377d925fba0/>
  <Fragment>
  <Button_5cbb2952409d1e5ed6e42602daa56ec7/>
  <Box sx={{"fontSize": "10px", "position": "fixed", "right": "25px", "top": "100px", "left": "350px"}}>
  <VStack>
  <Spacer/>
  <Grid_877aaff9bcb56b5c7ab5a50dfebbfc00/>
</VStack>
</Box>
  <Box sx={{"position": "fixed", "height": "100%", "left": "0px", "top": "0px", "zIndex": "500"}}>
  <VStack sx={{"width": "250px", "paddingX": "2em", "paddingY": "1em"}}>
  <ChakraImage src={`/logo.ico`} sx={{"width": "auto", "height": "auto", "margin": "0 auto"}}/>
  <Spacer/>
  <Heading_73213fd57920090aa2f067d6bb5028aa/>
  <Spacer/>
  <Text_0e668654e2c4c07b29717671d68b67d0/>
  <Text_18e2858f3f113be24440dab569919fe6/>
  <Text_2bb435c98cbb85d29f68337cd327b186/>
  <Spacer/>
  <Button_ada31a03f76209a573d1a66423fa4bed/>
  <Button_87a012435755203bce2f4d92b11c7acf/>
  <Alertdialog_c96281feaf3b7cbd9261d92fb8b998ee/>
</VStack>
</Box>
</Fragment>
  <NextHead>
  <title>
  {`Managment Site`}
</title>
  <meta content={`A Reflex app.`} name={`description`}/>
  <meta content={`favicon.ico`} property={`og:image`}/>
</NextHead>
</Fragment>
  )
}
