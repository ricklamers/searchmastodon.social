const INSTANCES_SOCIAL_URL = "https://instances.social/api/1.0/instances/list?" + 
  "include_down=false" + 
  "&include_dead=false" + 
  "&count=0";

const fetch = require('node-fetch');
const fs = require('fs');


async function main(){

  const response = await fetch(INSTANCES_SOCIAL_URL, {
    headers: [['Authorization', 'Bearer ' + process.env.INSTANCES_SOCIAL_SECRET]]
  });
  
  const body = await response.json();

  fs.writeFileSync('../docs/instances.json', JSON.stringify(body, 0, 2));
}

main()