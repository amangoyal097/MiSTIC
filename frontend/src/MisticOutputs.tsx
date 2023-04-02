import React from 'react'
import { Grid, Button } from '@mui/material'

const MisticOutput: React.FC<{
  images: any
  handleNext: () => void
  handleBack: () => void
}> = ({ images, handleNext, handleBack }) => {
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
        <Grid container spacing={2}>
          <Grid item xs={12} sm={6}>
            <Button fullWidth onClick={() => handleBack()}>
              Back
            </Button>
          </Grid>
          <Grid item xs={12} sm={6}>
            <Button variant="contained" fullWidth onClick={() => handleNext()}>
              Next
            </Button>
          </Grid>
        </Grid>
      </Grid>
    </Grid>
  )
}

export default MisticOutput
