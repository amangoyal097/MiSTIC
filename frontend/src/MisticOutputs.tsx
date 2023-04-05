import React from 'react'
import { Grid, Button } from '@mui/material'
import axios from 'axios'

const MisticOutput: React.FC<{
  images: any
  handleNext: () => void
  handleBack: () => void
}> = ({ images, handleNext, handleBack }) => {
  const getOutputs = () => {
    axios
      .get('http://localhost:5000/getOutputs', {
        responseType: 'blob',
      })
      .then((response) => {
        const url = window.URL.createObjectURL(new Blob([response.data]))
        const link = document.createElement('a')
        link.href = url
        link.setAttribute('download', `outputs.zip`)

        document.body.appendChild(link)
        link.click()
        link.parentNode!.removeChild(link)
      })
  }

  return (
    <Grid container spacing={3} mb={3} alignItems="center">
      <Grid item xs={12}>
        <img
          src={
            images.boundary !== ''
              ? `data:image/jpeg;base64,${images.boundary}`
              : undefined
          }
          style={{ width: '100%' }}
        />
      </Grid>
      <Grid item xs={12}>
        <img
          src={
            images.zones !== ''
              ? `data:image/jpeg;base64,${images.zones}`
              : undefined
          }
          style={{ width: '100%' }}
        />
      </Grid>
      <Grid item xs={12}>
        <Button fullWidth variant="contained" onClick={() => getOutputs()}>
          Download shapefiles and images
        </Button>
      </Grid>
      <Grid item xs={12}>
        <Grid container spacing={2}>
          <Grid item xs={12} sm={12}>
            <Button fullWidth variant="outlined" onClick={() => handleBack()}>
              Back
            </Button>
          </Grid>
          {/* <Grid item xs={12} sm={6}>
            <Button variant="contained" fullWidth onClick={() => handleNext()}>
              Next
            </Button>
          </Grid> */}
        </Grid>
      </Grid>
    </Grid>
  )
}

export default MisticOutput
