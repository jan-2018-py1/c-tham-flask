$(document).ready(function(){
    $("#enter").click(function(){
        console.log('test');
        {% if colour == 'blue' %}
        {%      set title = 'You chose Leonardo!' %}
        {%      set image = 'img/leonardo.jpg' %}
        {% elif colour == 'orange' %}
        {%      set title = 'You chose Michelangelo!' %}
        {%      set image = 'img/michelangelo.jpg' %}
        {% elif colour == 'red' %}
        {%      set title = 'You chose Raphael!' %}
        {%      set image = 'img/raphael.jpg' %}
        {% elif colour == 'purple': %}
        {%      set title = 'You chose Donatello!' %}
        {%      set image = 'img/donatello.jpg' %}
        {% else %}
        {%      set title = "There's no ninja in that color!" %}
        {%      set image = 'img/notapril.jpg' %}
        {% endif %}
    })
});