const express = require("express")
const app = express() 
const crypto = require('crypto') 


const secretkey1 = '1'; 
const secretkey2 = '2'; 


const body_parser = require("body-parser") 

app.use(body_parser.json()) 

const fingerprints = ["Syn-Fingerprint", "Krnl-Fingerprint"]
let HWID = ["b1119b01a0a3ea7d3d928d00b0f85cbc711935c7243a9de752112b07cc715423d33bdce4973660db553d28f1ab23535ee04c9bded02ce02fb69a31f21464e", ""]


const hmac = (secret, data) => {
       const hash = crypto.createHash('sha512');
       hash.update(secret + data + secret);
       return hash.digest('hex').toString();
   };

   
app.get("/", function(req, res) {
              return res.status(404).send(
                     JSON.stringify({success:false,message:"uwu"})
              )
})

app.get("/authenticate", function(req, res) {
       for (hwid of fingerprints) {
              if (req.headers[hwid.toLowerCase()]) {
                     HWID = req.headers[hwid.toLowerCase()]
                   res.write(hmac('success' + secretkey1, secretkey2)); 
              }
       } 
       (HWID == "")
              return res.status(404).send(
                     JSON.stringify({success:false,message:"uwu"})
              )
       }
)

const port = 5000;

app.listen(port, () => {
    console.log('Listening to: ', port)
});
