import React from 'react'
import { Grid, Button, TextField, Typography } from '@mui/material'
import axios from 'axios'

interface CoreData {
  itf: string
  minSupport: string
  max_Prune: string[]
  min_Freq: string[]
}

const CoreAnalysisInput: React.FC<{
  handleNext: () => void
  handleBack: () => void
}> = ({ handleNext, handleBack }) => {
  const [data, setData] = React.useState<CoreData>({
    itf: '10',
    minSupport: '10',
    max_Prune: ['30', '70'],
    min_Freq: ['10', '40'],
  })
  const [validating, setValidating] = React.useState<boolean>(false)
  const [loading, setLoading] = React.useState<boolean>(false)

  const validateNumber = (value: string) => {
    if (value === '') return false
    const num = parseInt(value)
    if (num < 0) return false
    return true
  }

  const validateGreater = (val1: string, val2: string) => {
    const num1 = parseInt(val1)
    const num2 = parseInt(val2)
    return num2 >= num1
  }

  const validateData = (request: CoreData) => {
    return (
      validateNumber(request.itf) &&
      validateNumber(request.minSupport) &&
      validateNumber(request.max_Prune[0]) &&
      validateNumber(request.max_Prune[1]) &&
      validateNumber(request.min_Freq[0]) &&
      validateNumber(request.min_Freq[1])
    )
  }

  const startCoreAnalysis = (request: CoreData) => {
    setValidating(true)
    if (!validateData(request)) return
    setValidating(false)
    let formData = new FormData()
    formData.append('itf', request.itf)
    formData.append('minSupport', request.minSupport)
    formData.append('maxPrune', request.max_Prune.toString())
    formData.append('minFreq', request.min_Freq.toString())

    const config = {
      headers: { 'content-type': 'multipart/form-data' },
    }
    setLoading(true)
    axios
      .post('http://localhost:5000/coreAnalysis', formData, config)
      .then((response) => {
        setLoading(false)
        handleNext()
      })
      .catch((err) => {
        console.log(err)
        setLoading(false)
      })
  }

  return (
    <Grid container spacing={2} mb={3}>
      <Grid item xs={12}>
        <Typography variant="h6" component="h6" sx={{ fontWeight: 400 }}>
          *All values should be in percentage
        </Typography>
      </Grid>
      <Grid item xs={12} mb={3}>
        <Grid container spacing={2}>
          <Grid item xs={12} sm={6}>
            <TextField
              required
              label="Initial Threshold Frequency"
              type="number"
              fullWidth
              variant="standard"
              value={data.itf}
              error={validating && !validateNumber(data.itf)}
              helperText={
                validating && !validateNumber(data.itf) && 'Invalid value'
              }
              onChange={(e) => setData({ ...data, itf: e.target.value })}
            />
          </Grid>
          <Grid item xs={12} sm={6}>
            <TextField
              required
              label="Minimum Support"
              type="number"
              fullWidth
              variant="standard"
              value={data.minSupport}
              error={validating && !validateNumber(data.minSupport)}
              helperText={
                validating &&
                !validateNumber(data.minSupport) &&
                'Invalid value'
              }
              onChange={(e) => setData({ ...data, minSupport: e.target.value })}
            />
          </Grid>
          <Grid item xs={12}>
            <Grid container spacing={2}>
              <Grid item xs={6}>
                <TextField
                  required
                  label="Max Prune : Lower Bound"
                  type="number"
                  fullWidth
                  variant="standard"
                  value={data.max_Prune[0]}
                  error={validating && !validateNumber(data.max_Prune[0])}
                  helperText={
                    validating &&
                    !validateNumber(data.max_Prune[0]) &&
                    'Invalid value'
                  }
                  onChange={(e) =>
                    setData({
                      ...data,
                      max_Prune: [e.target.value, data.max_Prune[1]],
                    })
                  }
                />
              </Grid>
              <Grid item xs={6}>
                <TextField
                  required
                  label="Max Prune : Upper Bound"
                  type="number"
                  fullWidth
                  variant="standard"
                  value={data.max_Prune[1]}
                  error={
                    validating &&
                    (!validateNumber(data.max_Prune[1]) ||
                      !validateGreater(data.max_Prune[0], data.max_Prune[1]))
                  }
                  helperText={
                    validating &&
                    (!validateNumber(data.max_Prune[1]) ||
                      !validateGreater(data.max_Prune[0], data.max_Prune[1])) &&
                    'Invalid value'
                  }
                  onChange={(e) =>
                    setData({
                      ...data,
                      max_Prune: [data.max_Prune[0], e.target.value],
                    })
                  }
                />
              </Grid>
            </Grid>
          </Grid>
          <Grid item xs={12}>
            <Grid container spacing={2}>
              <Grid item xs={6}>
                <TextField
                  required
                  label="Minimum Frequency : Lower Bound"
                  type="number"
                  fullWidth
                  variant="standard"
                  value={data.min_Freq[0]}
                  error={validating && !validateNumber(data.min_Freq[0])}
                  helperText={
                    validating &&
                    !validateNumber(data.min_Freq[0]) &&
                    'Invalid value'
                  }
                  onChange={(e) =>
                    setData({
                      ...data,
                      min_Freq: [e.target.value, data.min_Freq[1]],
                    })
                  }
                />
              </Grid>
              <Grid item xs={6}>
                <TextField
                  required
                  label="Minimum Frequency : Upper Bound"
                  type="number"
                  fullWidth
                  error={
                    validating &&
                    (!validateNumber(data.min_Freq[1]) ||
                      !validateGreater(data.min_Freq[0], data.min_Freq[1]))
                  }
                  variant="standard"
                  value={data.min_Freq[1]}
                  helperText={
                    validating &&
                    (!validateNumber(data.min_Freq[1]) ||
                      !validateGreater(data.min_Freq[0], data.min_Freq[1])) &&
                    'Invalid value'
                  }
                  onChange={(e) =>
                    setData({
                      ...data,
                      min_Freq: [data.min_Freq[0], e.target.value],
                    })
                  }
                />
              </Grid>
            </Grid>
          </Grid>
        </Grid>
      </Grid>
      <Grid item xs={12}>
        <Grid container spacing={2}>
          <Grid item xs={12} sm={6}>
            <Button fullWidth variant="outlined" onClick={() => handleBack()}>
              Back
            </Button>
          </Grid>
          <Grid item xs={12} sm={6}>
            <Button
              fullWidth
              variant="contained"
              onClick={() => startCoreAnalysis(data)}
            >
              run core analysis
            </Button>
          </Grid>
        </Grid>
      </Grid>
    </Grid>
  )
}

export default CoreAnalysisInput
