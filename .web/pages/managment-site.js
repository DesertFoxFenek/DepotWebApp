/** @jsxImportSource @emotion/react */


import { Fragment, useContext } from "react"
import { Button_5cbb2952409d1e5ed6e42602daa56ec7, Fragment_fd0e7cb8f9fb4669a6805377d925fba0 } from "/utils/stateful_components"
import { Box, Heading, Image as ChakraImage, Spacer, Text, VStack } from "@chakra-ui/react"
import "focus-visible/dist/focus-visible"
import "gridjs/dist/theme/mermaid.css"
import { Grid as DataTableGrid } from "gridjs-react"
import { StateContexts } from "/utils/context"
import NextHead from "next/head"



export function Text_2bb435c98cbb85d29f68337cd327b186 () {
  const state__sidebar_state = useContext(StateContexts.state__sidebar_state)


  return (
    <Text>
  {state__sidebar_state.brigades_num}
</Text>
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

export function Heading_73213fd57920090aa2f067d6bb5028aa () {
  const state__sidebar_state = useContext(StateContexts.state__sidebar_state)


  return (
    <Heading sx={{"textAlign": "center", "marginBottom": "1em"}}>
  {state__sidebar_state.depot_name}
</Heading>
  )
}

export function Grid_1dbd91505e7a0e8369ff4893dd672a98 () {
  const state__data_table_state = useContext(StateContexts.state__data_table_state)


  return (
    <DataTableGrid columns={state__data_table_state.columns} data={state__data_table_state.data} pagination={true} search={true}/>
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

export default function Component() {

  return (
    <Fragment>
  <Fragment_fd0e7cb8f9fb4669a6805377d925fba0/>
  <Fragment>
  <Button_5cbb2952409d1e5ed6e42602daa56ec7/>
  <Box sx={{"position": "fixed", "right": "25px", "top": "100px", "left": "350px"}}>
  <VStack>
  <Spacer/>
  <Grid_1dbd91505e7a0e8369ff4893dd672a98/>
</VStack>
</Box>
  <Box sx={{"position": "fixed", "height": "100%", "left": "0px", "top": "0px", "zIndex": "500"}}>
  <VStack sx={{"width": "250px", "paddingX": "2em", "paddingY": "1em"}}>
  <ChakraImage src={`/favicon.ico`} sx={{"margin": "0 auto"}}/>
  <Heading_73213fd57920090aa2f067d6bb5028aa/>
  <Spacer/>
  <Text_0e668654e2c4c07b29717671d68b67d0/>
  <Text_18e2858f3f113be24440dab569919fe6/>
  <Text_2bb435c98cbb85d29f68337cd327b186/>
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
