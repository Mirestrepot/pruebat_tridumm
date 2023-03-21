import axios from 'axios'

const getAPi = axios.create({
    baseURL: 'http://127.0.0.1:8000',
    timeout: 1000,
})

export { getAPi }