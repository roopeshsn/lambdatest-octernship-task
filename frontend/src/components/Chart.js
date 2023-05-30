import React from 'react';
import Plot from 'react-plotly.js';


export default function Chart() {
  const data = [
    {
      x: [1],
      y: [4],
      type: 'scatter',
      mode: 'markers',
      marker: {color: 'red'},
    },
    {
      x: [1],
      y: [6],
      type: 'scatter',
      mode: 'markers',
      marker: {color: 'orange'},
    },
  ]

  const layout= {width: 720, height: 360, title: 'A Fancy Plot'}

  return (
    <div>
      <Plot data={data} layout={layout}/>
    </div>
  )
}

