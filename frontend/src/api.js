import axios from 'axios'

const textGuardAPI = axios.create({
    baseURL: 'https://textguardapi-production.up.railway.app/api/v1'
})

export const postPredict=(text,contentType)=>{
    return textGuardAPI.post("/predictions/",{text, content_type:contentType})
    .then(({data})=>{
        return data
    })
}

export const getAllPredict=()=>{
    return textGuardAPI.get("/predictions/")
    .then(({data})=>{
        return data
    })
}