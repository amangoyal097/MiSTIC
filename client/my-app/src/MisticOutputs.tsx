import React from 'react'
import { Grid, Button, Typography } from '@mui/material'
import axios from 'axios'
import Carousel from 'react-material-ui-carousel'

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
    <Grid container spacing={2} mb={3} alignItems="center">
      {images && (
        <Grid item xs={12}>
          <Carousel
            navButtonsAlwaysVisible={true}
            autoPlay={false}
            navButtonsProps={{
              style: {
                marginTop: 'calc(700% - 40px)',
              },
            }}
          >
            {Object.keys(images).map((year) => (
              <Grid
                container
                key={year}
                justifyContent="center"
                p={{ xs: 2, md: 3 }}
              >
                <Grid item xs={12}>
                  <Typography component="h1" variant="h4" align="center">
                    {year}
                  </Typography>
                </Grid>
                <Grid item xs={12}>
                  <Typography
                    component="h1"
                    variant="h5"
                    align="left"
                    sx={{ borderBottom: '1px solid black' }}
                  >
                    Boundaries
                  </Typography>
                </Grid>
                <Grid item xs={12} md={8}>
                  <img
                    src={
                      images.boundary !== ''
                        ? `data:image/jpeg;base64,${images[year].boundaries}`
                        : undefined
                    }
                    style={{ width: '100%' }}
                  />
                </Grid>
                <Grid item xs={12}>
                  <Typography
                    component="h1"
                    variant="h5"
                    align="left"
                    sx={{ borderBottom: '1px solid black' }}
                  >
                    Zones
                  </Typography>
                </Grid>
                <Grid item xs={12} md={8}>
                  <img
                    src={
                      images.zones !== ''
                        ? `data:image/jpeg;base64,${images[year].zones}`
                        : undefined
                    }
                    style={{ width: '100%' }}
                  />
                </Grid>
              </Grid>
            ))}
          </Carousel>
        </Grid>
      )}
      <Grid item xs={12}>
        <Button fullWidth variant="contained" onClick={() => getOutputs()}>
          Download shapefiles and images
        </Button>
      </Grid>
      <Grid item xs={12}>
        <Grid container spacing={2}>
          <Grid item xs={12} sm={6}>
            <Button fullWidth variant="outlined" onClick={() => handleBack()}>
              Back
            </Button>
          </Grid>
          <Grid item xs={12} sm={6}>
            <Button fullWidth variant="contained" onClick={() => handleNext()}>
              Next
            </Button>
          </Grid>
        </Grid>
      </Grid>
    </Grid>
  )
}

export default MisticOutput
