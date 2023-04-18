import React from 'react'
import { Grid, Button, MenuItem, TextField } from '@mui/material'
import axios from 'axios'
import Loading from './Loading'
interface Data {
  startYear: string
  endYear: string
  type: string
  outputProj: string
  shpFile: File | undefined
}

const MisticForm: React.FC<{
  handleNext: () => void
  setImages: React.Dispatch<React.SetStateAction<any>>
}> = ({ handleNext, setImages }) => {
  const [data, setData] = React.useState<Data>({
    startYear: '2001',
    endYear: '2010',
    type: 'Max',
    outputProj: '3577',
    shpFile: undefined,
  })
  const [validating, setValidating] = React.useState<boolean>(false)
  const [loading, setLoading] = React.useState<boolean>(false)

  const validateNumber = (value: string) => {
    if (value === '') return false
    const num = parseInt(value)
    if (num <= 0) return false
    return true
  }

  const validateGreater = (val1: string, val2: string) => {
    const num1 = parseInt(val1)
    const num2 = parseInt(val2)
    return num2 >= num1
  }

  const validateData = (request: Data) => {
    return (
      validateNumber(request.startYear) &&
      validateNumber(request.endYear) &&
      validateGreater(request.startYear, request.endYear) &&
      validateNumber(request.outputProj) &&
      request.shpFile
    )
  }

  const startMistic = (request: Data) => {
    setValidating(true)
    if (!validateData(request)) return
    setValidating(false)
    let formData = new FormData()
    formData.append('startYear', request.startYear)
    formData.append('endYear', request.endYear)
    formData.append('type', request.type)
    formData.append('outputProj', request.outputProj)
    formData.append('file', request.shpFile!)

    const config = {
      headers: { 'content-type': 'multipart/form-data' },
    }
    setLoading(true)
    axios
      .post('http://localhost:5000/mistic', formData, config)
      .then((response) => {
        setImages(response.data.results)
        setLoading(false)
        handleNext()
      })
      .catch((err) => {
        console.log(err)
        setLoading(false)
      })
  }

  return (
    <React.Fragment>
      {loading && <Loading />}
      <Grid container spacing={3} mb={3} alignItems="center">
        <Grid item xs={12}>
          <Grid container spacing={2}>
            <Grid item xs={12} sm={4}>
              <TextField
                required
                label="Start Year"
                type="number"
                fullWidth
                variant="standard"
                value={data.startYear}
                error={validating && !validateNumber(data.startYear)}
                helperText={
                  validating &&
                  !validateNumber(data.startYear) &&
                  'Invalid value'
                }
                onChange={(e) =>
                  setData({ ...data, startYear: e.target.value })
                }
              />
            </Grid>
            <Grid item xs={12} sm={4}>
              <TextField
                required
                label="End Year"
                type="number"
                fullWidth
                variant="standard"
                value={data.endYear}
                error={
                  validating &&
                  (!validateNumber(data.endYear) ||
                    !validateGreater(data.startYear, data.endYear))
                }
                helperText={
                  validating &&
                  (!validateNumber(data.endYear) ||
                    !validateGreater(data.startYear, data.endYear)) &&
                  'Invalid value'
                }
                onChange={(e) => setData({ ...data, endYear: e.target.value })}
              />
            </Grid>
            <Grid item xs={12} sm={4}>
              <TextField
                select
                label="Type"
                fullWidth
                variant="standard"
                value={data.type}
                onChange={(e) => setData({ ...data, type: e.target.value })}
              >
                <MenuItem value={'Max'}>Max</MenuItem>
                <MenuItem value={'Min'}>Min</MenuItem>
              </TextField>
            </Grid>
          </Grid>
        </Grid>
        <Grid item xs={12}>
          <TextField
            required
            label="Output EPSG no."
            type="number"
            fullWidth
            variant="standard"
            value={data.outputProj}
            error={validating && !validateNumber(data.outputProj)}
            helperText={
              validating && !validateNumber(data.endYear) && 'Invalid value'
            }
            onChange={(e) => setData({ ...data, outputProj: e.target.value })}
          />
        </Grid>
        <Grid item xs={12}>
          <Grid container alignItems="center" spacing={2}>
            <Grid item xs={12} sm={6}>
              {data.shpFile ? data.shpFile.name : 'No File Selected'}
            </Grid>
            <Grid item xs={12} sm={6}>
              <Button
                fullWidth
                variant="contained"
                sx={{ background: '#24a0ed' }}
                component="label"
              >
                UPLOAD Map (.zip)
                <input
                  type="file"
                  onChange={(e) => {
                    setData({ ...data, shpFile: e.target.files![0] })
                  }}
                  hidden
                  accept=".zip"
                />
              </Button>
            </Grid>
          </Grid>
        </Grid>
        <Grid item xs={12}>
          <Button
            variant="contained"
            fullWidth
            onClick={() => startMistic(data)}
          >
            Start MiSTIC
          </Button>
        </Grid>
      </Grid>
    </React.Fragment>
  )
}
export default MisticForm
