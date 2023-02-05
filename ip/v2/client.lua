local http_request = http_request or request
if (syn) then
    http_request = syn.request    
end

local getresponse = http_request({
    Url = "http://nigger.com:5000/whitelist/auth",
   Method = 'GET';
   }).StatusCode  

if getresponse == 200 then 
    print('Success')
else
    return -- // not whitelisted
end
