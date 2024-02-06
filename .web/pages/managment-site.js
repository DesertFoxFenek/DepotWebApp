/** @jsxImportSource @emotion/react */


import { Fragment } from "react"
import { Button_5cbb2952409d1e5ed6e42602daa56ec7, Fragment_fd0e7cb8f9fb4669a6805377d925fba0 } from "/utils/stateful_components"
import { Box, Heading, Image as ChakraImage, Spacer, Text, VStack } from "@chakra-ui/react"
import "focus-visible/dist/focus-visible"
import NextHead from "next/head"



export default function Component() {

  return (
    <Fragment>
  <Fragment_fd0e7cb8f9fb4669a6805377d925fba0/>
  <Fragment>
  <Button_5cbb2952409d1e5ed6e42602daa56ec7/>
  <Box sx={{"position": "fixed", "height": "100%", "left": "0px", "top": "0px", "zIndex": "500"}}>
  <VStack sx={{"width": "250px", "paddingX": "2em", "paddingY": "1em"}}>
  <ChakraImage src={`/favicon.ico`} sx={{"margin": "0 auto"}}/>
  <Heading sx={{"textAlign": "center", "marginBottom": "1em"}}>
  {`Sidebar`}
</Heading>
  <Spacer/>
  <Text>
  {`Pole1`}
</Text>
  <Text>
  {`Pole2`}
</Text>
  <Text>
  {`Pole3`}
</Text>
  <Text>
  {`Pole4`}
</Text>
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
