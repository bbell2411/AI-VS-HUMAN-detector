import axios from 'axios'

const textGuardAPI = axios.create({
    baseURL: 'https://textguardapi-production.up.railway.app/api/v1'
})

export const postPredict=(text,contentType)=>{
    return textGuardAPI.post("/predictions/",{text, content_type:contentType})
    .then(({data})=>{
        console.log(data,"innn")
        // return data
    })
}