const {MongoClient} = require("mongodb");
const {Chart} = require("chart.js/auto")

require('dotenv').config();
console.log(process.env)

async function getDb(client){
    coll = await client.db("reddit_posts").collection("posts");
    cursor = coll.find({})
    const allValues = await cursor.toArray();
    console.log(allValues.length)
    const p = []
    const n = []
    allValues.forEach(function (d){
        if(d.score<=0){
            n.push(d)
        }
        else{
            p.push(d)
        }
    })
    const data = [p, n]
    return data

}



async function main(){
    const uri = process.env.MONGO_URI;
    console.log("uri", uri)
    // an instance of mongolient
    const client = new MongoClient(uri)
    try{
        await client.connect();
        data = await getDb(client);
        

    }
    catch(e){
        console.error(e)
    }
    finally {
        await client.close();
        
    
    }

    new Chart(
        document.getElementById("myChart"),
        {
            type:'bar',
            data:{
                labels: ["positive", "negative"],
                datasets:[
                    {
                        label:"Sentiment analysis ",
                        data: data
                    }
                ]
            }
        }
    )
}

main().catch(console.error)

// """
// """
/* 
<script cursor={{cursor}}>
            const ctx = document.getElementById('myChart');
           const p=[]
           const n = []
           cusror.forEach(element => {
            if(element<=0){
                n.push(element)
            }
            else{
                p.push(element)
            }
           });
           data = [p, n]
            new Chart(ctx,  {
            type:'bar',
            data:{
                labels: ["positive", "negative"],
                datasets:[
                    {
                        label:"Sentiment analysis ",
                        data: data
                    }
                ]
            }
        });
            </script>
*/