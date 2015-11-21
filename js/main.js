var Zone = Class.extend({
  init: function(name){
    // Variables
    this.name = name;
    this.$element = $('#' + name);
    console.log(this.$element);
    this.$sprinkleButton = this.$element.find('.sprinkle');
    this.$lampButton = this.$element.find('.lamp');
    console.log(this.$lampButton);
    this.$icon = this.$element.find('.icon');

    // Listeners
    this.$lampButton.on('click', this.onClickLampButton);
  },
  
  onClickLampButton: function() {
    console.log(this.name);
    this.$lampButton.addClass('active');
  }
});

var Pump = Class.extend({
  init: function(name){
    // Variables
    this.name = name;
    this.$element = $(name);
  },

  doSomething: function() {

  }
});

var Counter = Class.extend({
  init: function(name){
    // Variables
    this.name = name;
    this.$element = $(name);
  },

  doSomething: function() {

  }
});

var EventLog = Class.extend({
  init: function(name){
    // Variables
    this.name = name;
    this.$element = $(name);
  },

  doSomething: function() {

  }
});

var Event = Class.extend({
  init: function(name){
    // Variables
    this.name = name;
    this.$element = $(name);
  },

  doSomething: function() {

  }
});


$(document).ready(function() {
    var potager = new Zone("potager");
    $('.async.button').click(function() {
        $(this).toggleClass('loading');
        $('.ui.modal').modal('show');
    });
    $('.progress').progress({
        value: 22,
        total: 100,
        text: {
            active  : 'Arrosage: {value} / {total} litres',
            success : '{total} Arrosage terminé!'
        }
    });
});
