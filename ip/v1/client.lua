
local http_request = http_request or request
if (syn) then
    http_request = syn.request    
end

local timetoload = tick()

responses1 = "NFGJDFTRACTEDADBIAXVWWAHELXWHYDNNJOHYUWJHCSTFHONMK"
responses2 = "VMUIUWVCNXJHDPSJBUECNYPTJMRJOFSYIFRYTLOGJVIHZSWZDF"
responses3 = "HEAWZXCXBHVDRQADRJLAOOOFYAVRRXKCTEIBWJWRWGBJWCSIIV"



local Response = http_request({
 Url = "http://45.77.119.78:5000/whitelist/getresponse",
Method = 'GET';
}).Body

for _, v in pairs(responses) do
    if (Response == v) then
       print("Authenticated in "..string.format("%.7f", tostring(tick() - timetoload,nil)))
else
return -- // not whitelisted
    end
end
