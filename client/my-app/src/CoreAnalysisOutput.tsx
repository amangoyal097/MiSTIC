import React from 'react'
import { Grid, Button, Typography } from '@mui/material'
import axios from 'axios'

const CoreAnalysisOutput: React.FC<{
  handleReset: () => void
  handleBack: () => void
}> = ({ handleReset, handleBack }) => {
  const getOutputs = () => {
    axios
      .get('http://localhost:5000/getCoreOutputs', {
        responseType: 'blob',
      })
      .then((response) => {
        const url = window.URL.createObjectURL(new Blob([response.data]))
        const link = document.createElement('a')
        link.href = url
        link.setAttribute('download', `coreOutputs.zip`)

        document.body.appendChild(link)
        link.click()
        link.parentNode!.removeChild(link)
      })
  }

  return (
    <Grid container spacing={2} mb={3} alignItems="center">
      <Grid item xs={12}>
        <Button fullWidth variant="contained" onClick={() => getOutputs()}>
          Download Core Analysis Outputs
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
            <Button fullWidth variant="contained" onClick={() => handleReset()}>
              Reset
            </Button>
          </Grid>
        </Grid>
      </Grid>
    </Grid>
  )
}

export default CoreAnalysisOutput
