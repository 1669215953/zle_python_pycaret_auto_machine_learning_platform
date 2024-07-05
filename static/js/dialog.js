
function closeDialog() {
    var configs = document.getElementsByClassName('config-item');
    for(var i = 0; i < configs.length; i++) {
      configs[i].style.display = 'none';
    }
    dialog.style.display = 'none';
  }
  function finishDialog() {
      var configs = document.getElementsByClassName('config-item');
      for(var i = 0; i < configs.length; i++) {
        configs[i].style.display = 'none';
      }
      dialog.style.display = 'none';
      // 加载 JSON 文件
      axios.defaults.baseURL = 'http://127.0.0.1:5000';
      // 当按钮被点击时发送 JSON 数据
      // 加载 JSON 文件
      axios.get('./test.json')
        .then(function(response) {
            var jsonData = response.data;
            
            // 使用 axios 发送 POST 请求
            axios.post('/api/get-userparams', JSON.stringify(jsonData), {
                headers: {
                    'Content-Type': 'application/json'
                }
            })
            .then(function(response) {
                console.log('Response:', response);
            })
            .catch(function(error) {
                console.error('Error:', error);
            });
        })
        .catch(function(error) {
            console.error('Error:', error);
        });
        loadNewPage();//跳转页面

    }


    function switchConfig(oldConfig, newConfig) {
      saveFormState(oldConfig);
      document.getElementById(oldConfig).style.display = 'none';
      document.getElementById(newConfig).style.display = 'block';
      var headings = document.getElementsByClassName('step');
      for (var i = 0; i < headings.length; i++) {
        if (headings[i].classList.contains('current')) {
          headings[i].classList.remove('current');
          var nextIndex = (i + 1) % headings.length;
          headings[nextIndex].classList.add('current');
          break;
        }
      }  
      loadFormState(newConfig);
    }
    
    
    function saveFormState(config) {
      var inputs = document.getElementById(config).querySelectorAll('input, select');
    
      formStates[config] = {};
    
      inputs.forEach(input => {
        formStates[config][input.name] = input.value;
      });
    }
    
    function loadFormState(config) {
      if (formStates[config]) {
        var inputs = document.getElementById(config).querySelectorAll('input, select');
    
        inputs.forEach(input => {
          if (formStates[config][input.name] !== undefined) {
            input.value = formStates[config][input.name];
          }
        });
      }
    }
    
    // JSON Data
    var jsonData = [
      {
        "AUC": {
          "mode":"input",
          "default":"88.1"
        },
        "Accuracy":{
          "mode": "checkbox",
          "default":"checked"
        },
        "F1": {
          "mode": "select",
          "select_item":["one","two","three"],
          "default":"one"
        }
      },
      {
        "Precision": {
          "mode":"input",
          "default":"0.9"
        },
        "Recall":{
          "mode": "checkbox",
          "default":"checked"
        },
        "F2": {
          "mode": "select",
          "select_item":["four","five","six"],
          "default":"four"
        }
      },
      {
        "MCC": {
          "mode":"input",
          "default":"0.1"
        },
        "Kappa":{
          "mode": "checkbox",
          "default":"checked"
        },
        "F3": {
          "mode": "select",
          "select_item":["seven","eight","nine"],
          "default":"seven"
        }
      }
    ];
    
    for (var i = 0; i < jsonData.length; i++) {
      var form = document.getElementById('myForm' + (i+1));
      var data = jsonData[i];
    
      for (var key in data) {
        var div = document.createElement('div');
    
        var label = document.createElement('label');
        label.textContent = key;
        div.appendChild(label);
    
        switch (data[key].mode) {
          case 'input':
            var input = document.createElement('input');
            input.type = 'text';
            input.name = 'form' + (i+1) + '-' + key;
            input.value = data[key].default;
            div.appendChild(input);
            break;
          case 'checkbox':
            var input = document.createElement('input');
            input.type = 'checkbox';
            input.name = 'form' + (i+1) + '-' + key;
            input.className ="mycheck_button" 
            input.checked = (data[key].default === 'checked') ? true : false;
            div.appendChild(input);
            break;
          case 'select':
            var select = document.createElement('select');
            select.name = 'form' + (i+1) + '-' + key;
            for (var j = 0; j < data[key].select_item.length; j++) {
              var option = document.createElement('option');
              option.value = data[key].select_item[j];
              option.text = data[key].select_item[j];
              if (data[key].select_item[j] === data[key].default) {
                option.selected = true;
              }
              select.appendChild(option);
            }
            div.appendChild(select);
            break;
        }
    
        form.appendChild(div);
      }
    }
var dialog = document.getElementById('dialog');
var formStates = {};
// Config Dialog related functions
function openDialog(currentConfig) {
if (!formStates[currentConfig]) {
  formStates[currentConfig] = {};
}
var headings = document.getElementsByClassName('step');
for (var i = 0; i < headings.length; i++) {
  if (headings[i].classList.contains('current')) {
    headings[i].classList.remove('current');

  }
}  
document.getElementById(currentConfig).style.display = 'block';
dialog.style.display = 'block';
document.getElementById('step-1').classList.add('current'); 
loadFormState(currentConfig);
}