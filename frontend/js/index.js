setRankComponent()
setStatisticsComponent()
setFooterRankComponent()

function setRankComponent() {
  setBottleneckRankComponent()
  setBestRankComponent()
}

function setBottleneckRankComponent() {
  var vara_id = 1
  getVaraByID(vara_id, (json)=>{
    $('#bottleneck-mov-1-source').html(json.worst_steps[0].origin)
    $('#bottleneck-mov-1-description').html(json.worst_steps[0].med_time)
    $('#bottleneck-mov-1-dest').html(json.worst_steps[0].destination)

    $('#bottleneck-mov-2-source').html(json.worst_steps[1].origin)
    $('#bottleneck-mov-2-description').html(json.worst_steps[1].med_time)
    $('#bottleneck-mov-2-dest').html(json.worst_steps[1].destination)

    $('#bottleneck-mov-3-source').html(json.worst_steps[2].origin)
    $('#bottleneck-mov-3-description').html(json.worst_steps[2].med_time)
    $('#bottleneck-mov-3-dest').html(json.worst_steps[2].destination)

    //bottoleneck table
    $('#table-bottleneck-tab1').html(json.worst_steps[0].origin + '-' + json.worst_steps[0].destination)
    $('#table-bottleneck-tab2').html(json.worst_steps[1].origin + '-' + json.worst_steps[1].destination)
    $('#table-bottleneck-tab3').html(json.worst_steps[2].origin + '-' + json.worst_steps[2].destination)

    // Best varas on worst step 1
    getBestVarasOnStep(json.worst_steps[0].step_id,
        vara_id,
        10,
        (json2)=>{
          $('#table-bottleneck-row-1-name').html(json2[0].vara_name)
          $('#table-bottleneck-row-1-duration').html(json2[0].med_time)
          $('#table-bottleneck-row-1-comments').html(json2[0].comment)

          $('#table-bottleneck-row-2-name').html(json2[1].vara_name)
          $('#table-bottleneck-row-2-duration').html(json2[1].med_time)
          $('#table-bottleneck-row-2-comments').html(json2[1].comment)

          $('#table-bottleneck-row-3-name').html(json2[2].vara_name)
          $('#table-bottleneck-row-3-duration').html(json2[2].med_time)
          $('#table-bottleneck-row-3-comments').html(json2[2].comment)

          $('#table-bottleneck-row-4-name').html(json2[3].vara_name)
          $('#table-bottleneck-row-4-duration').html(json2[3].med_time)
          $('#table-bottleneck-row-4-comments').html(json2[3].comment)

          $('#table-bottleneck-row-5-name').html(json2[4].vara_name)
          $('#table-bottleneck-row-5-duration').html(json2[4].med_time)
          $('#table-bottleneck-row-5-comments').html(json2[4].comment)

          $('#table-bottleneck-row-6-name').html(json2[5].vara_name)
          $('#table-bottleneck-row-6-duration').html(json2[5].med_time)
          $('#table-bottleneck-row-6-comments').html(json2[5].comment)

          $('#table-bottleneck-row-7-name').html(json2[6].vara_name)
          $('#table-bottleneck-row-7-duration').html(json2[6].med_time)
          $('#table-bottleneck-row-7-comments').html(json2[6].comment)

          $('#table-bottleneck-row-8-name').html(json2[7].vara_name)
          $('#table-bottleneck-row-8-duration').html(json2[7].med_time)
          $('#table-bottleneck-row-8-comments').html(json2[7].comment)

          $('#table-bottleneck-row-9-name').html(json2[8].vara_name)
          $('#table-bottleneck-row-9-duration').html(json2[8].med_time)
          $('#table-bottleneck-row-9-comments').html(json2[8].comment)
        })
  })
  $('#bottleneck-mov-1-position').html('13'+'°')
  $('#bottleneck-mov-2-position').html('13'+'°')
  $('#bottleneck-mov-3-position').html('13'+'°')
}

function setBestRankComponent() {
  var vara_id = 1
  getVaraByID(vara_id,(json)=>{
    //best movements component
    $('#best-mov-1-source').html(json.best_steps[0].origin)
    $('#best-mov-1-description').html(json.best_steps[0].med_time)
    $('#best-mov-1-dest').html(json.best_steps[0].destination)

    $('#best-mov-2-source').html(json.best_steps[1].origin)
    $('#best-mov-2-description').html(json.best_steps[1].med_time)
    $('#best-mov-2-dest').html(json.best_steps[1].destination)

    $('#best-mov-3-source').html(json.best_steps[2].origin)
    $('#best-mov-3-description').html(json.best_steps[2].med_time)
    $('#best-mov-3-dest').html(json.best_steps[2].destination)

    //best movements table
    $('#table-best-tab1').html(json.best_steps[0].origin + '-' + json.best_steps[0].destination)
    $('#table-best-tab2').html(json.best_steps[1].origin + '-' + json.best_steps[1].destination)
    $('#table-best-tab3').html(json.best_steps[2].origin + '-' + json.best_steps[2].destination)

    // Best varas on best step 1
    getBestVarasOnStep(json.best_steps[0].step_id,
        vara_id,
        10,
        (json2)=>{
          $('#table-best-row-1-name').html(json2[0].vara_name)
          $('#table-best-row-1-duration').html(json2[0].med_time)
          $('#table-best-row-1-comments').html(json2[0].comment)

          $('#table-best-row-2-name').html(json2[1].vara_name)
          $('#table-best-row-2-duration').html(json2[1].med_time)
          $('#table-best-row-2-comments').html(json2[1].comment)

          $('#table-best-row-3-name').html(json2[2].vara_name)
          $('#table-best-row-3-duration').html(json2[2].med_time)
          $('#table-best-row-3-comments').html(json2[2].comment)

          $('#table-best-row-4-name').html(json2[3].vara_name)
          $('#table-best-row-4-duration').html(json2[3].med_time)
          $('#table-best-row-4-comments').html(json2[3].comment)

          $('#table-best-row-5-name').html(json2[4].vara_name)
          $('#table-best-row-5-duration').html(json2[4].med_time)
          $('#table-best-row-5-comments').html(json2[4].comment)

          $('#table-best-row-6-name').html(json2[5].vara_name)
          $('#table-best-row-6-duration').html(json2[5].med_time)
          $('#table-best-row-6-comments').html(json2[5].comment)

          $('#table-best-row-7-name').html(json2[6].vara_name)
          $('#table-best-row-7-duration').html(json2[6].med_time)
          $('#table-best-row-7-comments').html(json2[6].comment)

          $('#table-best-row-8-name').html(json2[7].vara_name)
          $('#table-best-row-8-duration').html(json2[7].med_time)
          $('#table-best-row-8-comments').html(json2[7].comment)

          $('#table-best-row-9-name').html(json2[8].vara_name)
          $('#table-best-row-9-duration').html(json2[8].med_time)
          $('#table-best-row-9-comments').html(json2[8].comment)
        })
  })
  //best movements component
  //best-mov-1-position
  //best-mov-2-position
  //best-mov-3-position
}

function setStatisticsComponent(){
  var vara_id = 1
  getVaraByID(vara_id, (json)=> {
    //worst
    $('#statistics-wrost-title-1').html('Pior <br>desempenho')
    $('#statistics-wrost-value').html(json.worst_steps[0].origin)
    $('#statistics-wrost-position').html('1' + '° de ' + json.group.amount_of_varas + ' varas')
    //statistics-wrost-title-2

    //best
    $('#statistics-best-title-1').html('Melhor <br>desempenho')
    $('#statistics-best-value').html(json.best_steps[0].origin)
    $('#statistics-best-position').html('1' + '° de ' + json.group.amount_of_varas + ' varas')
    //statistics-best-title-2

    //duration
    $('#statistics-duration-title-1').html('Duração da <br>baixa do processo')
    $('#statistics-duration-value').html(json.days_finish_process + ' dias')
    $('#statistics-duration-position').html('1' + '° de ' + json.group.amount_of_varas + ' varas')
    //statistics-duration-title-2

    //movements
    $('#statistics-moves-title-1').html('Movimentação <br>por processo')
    $('#statistics-moves-value').html(json.movements)
    //statistics-moves-title-2

    //finished
    $('#statistics-finished-title-1').html('Processos <br>julgados')
    $('#statistics-finished-value').html(json.finished_processes)
    $('#statistics-finished-position').html('1' + '° de ' + json.group.amount_of_varas + ' varas')
    //statistics-finished-title-2
  })
}

function setFooterRankComponent() {
  // $('#best-time-1').html('')
  //best-time-2
  //best-time-3
  //best-time-4
  //best-time-5
  //best-time-6
  //best-time-7
  //best-time-8
  //best-time-9
  //best-time-10
}
