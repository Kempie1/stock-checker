import React, {  useState, useEffect  } from 'react';
import {Line} from 'react-chartjs-2';
import axios from 'axios'
import {readFile} from 'fs';

const Chart = ()=>{
const [chart, setChart] = useState({})

useEffect(()=>{
    setChart(require('../../mocks/chart.json'))
    console.log(chart)
}, [])

/*const state = {
  labels: ['January', 'February', 'March',
           'April', 'May'],
  datasets: [
    {
      label: 'Rainfall',
      fill: false,
      lineTension: 0.5,
      backgroundColor: 'rgba(75,192,192,1)',
      borderColor: 'rgba(0,0,0,1)',
      borderWidth: 2,
      data: [65, 59, 80, 81, 56]
    }
  ]
}*/




    return (
      <div  className="stock_chart">
        <Line
          data={chart}
          options={{
            maintainAspectRatio: false ,
            title:{
              display:true,
              text:'Average Rainfall per month',
              fontSize:20
            }
          }}
        />
      </div>
    );
  }

export default Chart;