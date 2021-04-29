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
        {{ script }}
    </script>

    <style>
        {{ style }}
    </style>

</html>