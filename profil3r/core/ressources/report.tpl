<!DOCTYPE html>
<html>
  <head>
    <meta http-equiv="Content-Type" content="text/html;charset=utf-8"/>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <title>Profil3r</title>
  </head>

  <body>

        <div class="card" style="height:800px;">
            <section class="container">

                    <input type="search" class="light-table-filter searchbar" data-table="order-table" placeholder="Filter results">

                    <table class="order-table table">
                        <thead>
                            <tr>
                                <th>Service</th>
                                <th>Category</th>
                                <th>Link</th>
                                <th>Breached</th>
                            </tr>
                        </thead>
                        <tbody>

                            {% for service, accounts in results %}
                                {% for account in accounts["accounts"] %}
                                <tr>
                                    <td>{{ service }}</td>
                                    <td>{{ accounts["type"] }}</td>
                                    <td>    
                                        {% if (accounts["type"] == "email") %}
                                        <i>{{ account['value'] }}</i>
                                        {% else %}
                                        <a href="{{ account['value'] }}" target="_blank">{{ account['value'] }}</a> 
                                        {% endif %}
                                    </td>
                                    <td>
                                        {% if (accounts["type"] == "email") %}
                                            {% if account["breached"] %} 
                                            ✔️
                                            {% else %}
                                            ❌
                                            {% endif %}
                                        {% endif %}
                                    </td>
                                </tr>
                                {% endfor %}
                            {% endfor %}

                        </tbody>
                    </table>

                </section>

                <span class="footer">Profiler version {{ version }} - report was generated at {{ time }}</span>

            </div>
    </body>

    <script>

    (function(document) {
        'use strict';

        var LightTableFilter = (function(Arr) {

            var _input;

            function _onInputEvent(e) {
                _input = e.target;
                var tables = document.getElementsByClassName(_input.getAttribute('data-table'));
                Arr.forEach.call(tables, function(table) {
                    Arr.forEach.call(table.tBodies, function(tbody) {
                        Arr.forEach.call(tbody.rows, _filter);
                    });
                });
            }

            function _filter(row) {
                var text = row.textContent.toLowerCase(), val = _input.value.toLowerCase();
                row.style.display = text.indexOf(val) === -1 ? 'none' : 'table-row';
            }

                return {
                    init: function() {
                        var inputs = document.getElementsByClassName('light-table-filter');
                        Arr.forEach.call(inputs, function(input) {
                            input.oninput = _onInputEvent;
                        });
                    }
                };
            })(Array.prototype);

            document.addEventListener('readystatechange', function() {
                if (document.readyState === 'complete') {
                    LightTableFilter.init();
                }
            });

        })(document);

    </script>

    <style>
        body {
            background: #e2e1e0;
            text-align: center;
        }

        a[target="_blank"]::after {
            content: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAYAAACNMs+9AAAAQElEQVR42qXKwQkAIAxDUUdxtO6/RBQkQZvSi8I/pL4BoGw/XPkh4XigPmsUgh0626AjRsgxHTkUThsG2T/sIlzdTsp52kSS1wAAAABJRU5ErkJggg==);
            margin: 0 3px 0 5px;
        }

        .footer {
            text-align: center;
            margin: 5px;
            padding: 5px;
        }

        .card {
            background: #fff;
            border-radius: 2px;
            width: 80%; 
            max-width: 80%;  
            display: inline-block;
            margin: 1rem;
            position: relative;
            box-shadow: 0 1px 3px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.24);
            overflow-y: scroll;
        }
        
        .searchbar {
            display: block;
            font-weight:300;
            font-size: 25px;
            border:0px;
            outline: none;
            width: 40%;
            margin: 10px auto 10px auto;
            -webkit-box-sizing: border-box;
            -moz-box-sizing: border-box;
            box-sizing: border-box;
            color: #4b545f;
            background: #fff;
            padding: 10px 15px;
            -webkit-transition: all 0.1s ease-in-out;
            -moz-transition: all 0.1s ease-in-out;
            -ms-transition: all 0.1s ease-in-out;
            -o-transition: all 0.1s ease-in-out;
            transition: all 0.1s ease-in-out;
        }

        .searchbar:focus {
            border-bottom:1px solid #ddd;
        }
        
    </style>

</html>