

    // 发送ajax请求，从后台获取json数据
    
    function get_reward_Data() {
        $.ajax({
           url:'http://localhost:5000/page/woundcloud/reward',
           data:{},
           type:'GET',
           async:true,
           dataType:'json',
           success:function(data) {
        var myChart = echarts.init(document.getElementById('word-cloud-reward'));
         var maskImage = new Image();
         maskImage.src = data.image
   
         maskImage.onload = function(){
           myChart.setOption( {
             backgroundColor:'#fff',
             tooltip: {
               show: false
             },
             series: [{
               type: 'wordCloud',
               gridSize: 1,
               sizeRange: [12, 55],
               rotationRange: [-45, 0, 45, 90],
               maskImage: maskImage,
               textStyle: {
                 normal: {
                   color: function() {
                     return 'rgb(' +
                         Math.round(Math.random() * 255) +
                         ', ' + Math.round(Math.random() * 255) +
                         ', ' + Math.round(Math.random() * 255) + ')'
                   }
                 }
               },
               left: 'center',
               top: 'center',
               right: null,
               bottom: null,
               data: data.value
             }]
           })
         }

           },
           error:function (msg) {
               console.log(msg);
               console.log('词云系统发生错误');
           }
       })
   };
   function get_languages_Data() {
    $.ajax({
        url: 'http://localhost:5000/page/data/languages',
        type: 'GET',
        async: true,
        dataType: 'json',
        success: function (datas) {

            var myChart = echarts.init(document.getElementById('languages'));
            var totalText = "总计: "+datas.total
          console.log( datas,datas.total,datas.data)
            option = {
             title: {
                   text: '编程语言岗位占比',
                   left: 'center',
                   top: 5,
                   textStyle: {
                         color: '#333',
                         fontSize: 20
                   }
                },
                tooltip: {
                    trigger: 'item'
                },
                legend: {
                    top: '5%',
                    left: 'center'
                },
                graphic: [
                    {
                        type: 'text',
                        id: 'totalText',
                        left: 'center',
                        top: '49%',
                        zlevel: 2,
                        style: {
                            text: totalText,
                            textAlign: 'center',
                            fill: '#666',
                            fontSize: 25
                        }
                    }
                ],
                series: [
                    {
                        name: 'Access From',
                        type: 'pie',
                        radius: ['40%', '70%'],
                        avoidLabelOverlap: false,
                        itemStyle: {
                            borderRadius: 10,
                            borderColor: '#fff',
                            borderWidth: 2
                        },
                        label: {
                            show: false
                        },
                        emphasis: {
                            label: {
                                show: false,
                                fontSize: 40,
                                fontWeight: 'bold'
                            }
                        },
                        labelLine: {
                            show: false
                        },
                        data: datas.data
                    }
                ]
            };

            option && myChart.setOption(option);

            myChart.on('mouseover', function (params) {
                if (params.componentType === 'series') {
                    if (params.seriesType === 'pie') {
                        var hoveredData = params.data;
                        if (hoveredData) {
                            var detailText = hoveredData.name+': ' + hoveredData.value;
                            myChart.setOption({
                                graphic: {
                                    id: 'totalText',
                                    style: {
                                        text: detailText
                                    }
                                }
                            });
                        } else {
                            myChart.setOption({
                                graphic: {
                                    id: 'totalText',
                                    style: {
                                        text: totalText
                                    }
                                }
                            });
                        }
                    }
                }
            });

            myChart.on('mouseout', function (params) {
                myChart.setOption({
                    graphic: {
                        id: 'totalText',
                        style: {
                            text: totalText
                        }
                    }
                });
            });
        },
        error: function (msg) {
            console.log(msg);
            console.log('编程语言汇总出错发生错误');
        }
    });
}



function get_academic_Data() {
    $.ajax({
       url:'http://localhost:5000/page/data/academic',
       type:'GET',
       async:true,
       dataType:'json',
       success:function(datas) {
       var myChart = echarts.init(document.getElementById('main'));
       var option;
       option = {
       title: {
          text: '学历要求占比',
          subtext: '学历占比图',
          left: 'center'
       },
       tooltip: {
          trigger: 'item'
       },
       legend: {
          orient: 'vertical',
          left: 'left'
       },
       series: [
          {
          name: 'Access From',
          type: 'pie',
          radius: '50%',
          data:datas,
          emphasis: {
             itemStyle: {
             shadowBlur: 10,
             shadowOffsetX: 0,
             shadowColor: 'rgba(0, 0, 0, 0.5)'
             }
          }
          }
       ]
       };

       option && myChart.setOption(option);

       },
       error:function (msg) {
           console.log(msg);
           console.log('词云系统发生错误');
       }
   })
};
function getmapData() {
    $.ajax({
       url:'http://localhost:5000/page/chinamap',
       data:{},
       type:'GET',
       async:true,
       dataType:'json',
       success:function(mapdata) {
   // 初始化echarts实例
   var myEcharts = echarts.init(document.getElementById("china"));
var option = {
    title: {  //标题样式
        text: '中国地图',
        x: "center",
        textStyle: {
            fontSize: 18,
            color: "black"
        },
    },
    tooltip: {
        trigger: 'item',
        formatter: function (params) {
            //console.log(params)
            if (params.name) {
                return params.name + ' : ' + (isNaN(params.value) ? 0 : parseInt(params.value));
            }
        }
    },
    visualMap: {//视觉映射组件
        top: 'bottom',
        left: 'left',
        min: 10,
        max: 10000,
        //text: ['High', 'Low'],
        realtime: false,  //拖拽时，是否实时更新
        calculable: true,  //是否显示拖拽用的手柄
        inRange: {
            color: ['lightskyblue', 'yellow', 'orangered']
        }
    },
    series: [
        {
            name: '招聘岗位数据分布',
            type: 'map',
            mapType: 'china',
            roam: true,//是否开启鼠标缩放和平移漫游
            itemStyle: {//地图区域的多边形 图形样式
                normal: {//是图形在默认状态下的样式
                    label: {
                        show: true,//是否显示标签
                        textStyle: {
                            color: "black"
                        }
                    }
                },
                zoom: 1.5,  //地图缩放比例,默认为1
                emphasis: {//是图形在高亮状态下的样式,比如在鼠标悬浮或者图例联动高亮时
                    label: {show: true}
                }
            },
            top: "3%",//组件距离容器的距离
            data: mapdata
        }
    ]
};
// 使用刚指定的配置项和数据显示图表。
myEcharts.setOption(option);
       },
       error:function (msg) {
          console.log(msg);
          console.log('地图系统发生错误');
       }
    })
};

function get_capacity_Data() {
    $.ajax({
       url:'http://localhost:5000/page/woundcloud/capacity',
       data:{},
       type:'GET',
       async:true,
       dataType:'json',
       success:function(data) {
    var myChart = echarts.init(document.getElementById('word-cloud-capacity'));
     var maskImage = new Image();
     maskImage.src = data.image

     maskImage.onload = function(){
       myChart.setOption( {
         backgroundColor:'#fff',
         tooltip: {
           show: false
         },
         series: [{
           type: 'wordCloud',
           gridSize: 1,
           sizeRange: [12, 55],
           rotationRange: [-45, 0, 45, 90],
           maskImage: maskImage,
           textStyle: {
             normal: {
               color: function() {
                 return 'rgb(' +
                     Math.round(Math.random() * 255) +
                     ', ' + Math.round(Math.random() * 255) +
                     ', ' + Math.round(Math.random() * 255) + ')'
               }
             }
           },
           left: 'center',
           top: 'center',
           right: null,
           bottom: null,
           data: data.value
         }]
       })
     }

       },
       error:function (msg) {
           console.log(msg);
           console.log('词云系统发生错误');
       }
   })
};



function get_industry_Data() {
    $.ajax({
       url:'http://localhost:5000/page/woundcloud/industry',
       data:{},
       type:'GET',
       async:true,
       dataType:'json',
       success:function(data) {
    var myChart = echarts.init(document.getElementById('word-cloud-industry'));
     var maskImage = new Image();
     maskImage.src = data.image

     maskImage.onload = function(){
       myChart.setOption( {
         backgroundColor:'#fff',
         tooltip: {
           show: false
         },
         series: [{
           type: 'wordCloud',
           gridSize: 1,
           sizeRange: [12, 55],
           rotationRange: [-45, 0, 45, 90],
           maskImage: maskImage,
           textStyle: {
             normal: {
               color: function() {
                 return 'rgb(' +
                     Math.round(Math.random() * 255) +
                     ', ' + Math.round(Math.random() * 255) +
                     ', ' + Math.round(Math.random() * 255) + ')'
               }
             }
           },
           left: 'center',
           top: 'center',
           right: null,
           bottom: null,
           data: data.value
         }]
       })
     }

       },
       error:function (msg) {
           console.log(msg);
           console.log('词云系统发生错误');
       }
   })
};



function get_province_Data() {
    $.ajax({
       url:'http://localhost:5000/page/woundcloud/province',
       data:{},
       type:'GET',
       async:true,
       dataType:'json',
       success:function(data) {
    var myChart = echarts.init(document.getElementById('word-cloud-province'));
     var maskImage = new Image();
     maskImage.src = data.image

     maskImage.onload = function(){
       myChart.setOption( {
         backgroundColor:'#fff',
         tooltip: {
           show: false
         },
         series: [{
           type: 'wordCloud',
           gridSize: 1,
           sizeRange: [12, 55],
           rotationRange: [-45, 0, 45, 90],
           maskImage: maskImage,
           textStyle: {
             normal: {
               color: function() {
                 return 'rgb(' +
                     Math.round(Math.random() * 255) +
                     ', ' + Math.round(Math.random() * 255) +
                     ', ' + Math.round(Math.random() * 255) + ')'
               }
             }
           },
           left: 'center',
           top: 'center',
           right: null,
           bottom: null,
           data: data.value
         }]
       })
     }

       },
       error:function (msg) {
           console.log(msg);
           console.log('词云系统发生错误');
       }
   })
}



function get_hot_position_Data() {
    $.ajax({
        url: 'http://localhost:5000/page/data/hot_position',
        type: 'GET',
        async: true,
        dataType: 'json',
        success: function (datas) {

            var myChart = echarts.init(document.getElementById('hot_position'));
            var totalText = "总计: "+datas.total
          console.log( datas,datas.total,datas.data)
            option = {
             title: {
                   text: '热门岗位占比',
                   left: 'center',
                   top: 5,
                   textStyle: {
                         color: '#333',
                         fontSize: 20
                   }
                },
                tooltip: {
                    trigger: 'item'
                },
                legend: {
                    top: '5%',
                    left: 'center'
                },
                graphic: [
                    {
                        type: 'text',
                        id: 'totalText',
                        left: 'center',
                        top: '49%',
                        zlevel: 2,
                        style: {
                            text: totalText,
                            textAlign: 'center',
                            fill: '#666',
                            fontSize: 25
                        }
                    }
                ],
                series: [
                    {
                        name: 'Access From',
                        type: 'pie',
                        radius: ['40%', '70%'],
                        avoidLabelOverlap: false,
                        itemStyle: {
                            borderRadius: 10,
                            borderColor: '#fff',
                            borderWidth: 2
                        },
                        label: {
                            show: false
                        },
                        emphasis: {
                            label: {
                                show: false,
                                fontSize: 40,
                                fontWeight: 'bold'
                            }
                        },
                        labelLine: {
                            show: false
                        },
                        data: datas.data
                    }
                ]
            };

            option && myChart.setOption(option);

            myChart.on('mouseover', function (params) {
                if (params.componentType === 'series') {
                    if (params.seriesType === 'pie') {
                        var hoveredData = params.data;
                        if (hoveredData) {
                            var detailText = hoveredData.name+': ' + hoveredData.value;
                            myChart.setOption({
                                graphic: {
                                    id: 'totalText',
                                    style: {
                                        text: detailText
                                    }
                                }
                            });
                        } else {
                            myChart.setOption({
                                graphic: {
                                    id: 'totalText',
                                    style: {
                                        text: totalText
                                    }
                                }
                            });
                        }
                    }
                }
            });

            myChart.on('mouseout', function (params) {
                myChart.setOption({
                    graphic: {
                        id: 'totalText',
                        style: {
                            text: totalText
                        }
                    }
                });
            });
        },
        error: function (msg) {
            console.log(msg);
            console.log('编程语言汇总出错发生错误');
        }
    });
}


function get_job_time_Data() {
    $.ajax({
       url:'http://localhost:5000/page/data/job_time',
       data:{},
       type:'GET',
       async:true,
       dataType:'json',
       success:function(datas) {
    var myChart = echarts.init(document.getElementById('job_time'));
       option = {
        title: {
            text: '工作经验需求'
        },
        tooltip: {
          trigger: 'axis',
          axisPointer: {
            type: 'shadow'
          }
        },
        grid: {
          left: '3%',
          right: '4%',
          bottom: '3%',
          containLabel: true
        },
        xAxis: [
          {
            type: 'category',
            data: datas.x,
            axisTick: {
              alignWithLabel: true
            }
          }
        ],
        yAxis: [
          {
            type: 'value'
          }
        ],
        series: [
          {
            name: 'Direct',
            type: 'bar',
            barWidth: '60%',
            data: datas.y
          }
        ]
      };

        option && myChart.setOption(option);

       },
       error:function (msg) {
           console.log(msg);
           console.log('词云系统发生错误');
       }
   })
};




get_job_time_Data()










get_hot_position_Data()


get_province_Data()
setInterval(get_province_Data, 15000)//循环调用


get_industry_Data()
setInterval(get_industry_Data, 15000)//循环调用

get_reward_Data()
get_capacity_Data()
setInterval(getmapData, 1000)//循环调用
get_academic_Data()
get_languages_Data();
setInterval(get_reward_Data, 10000)//循环调用
setInterval(get_capacity_Data, 5000)//循环调用
