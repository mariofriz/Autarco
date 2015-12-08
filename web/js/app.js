new Vue({
    el: '#app',
    data: {
        zones: [
            {
                id: 0,
                name: "Potager",
                isWatering: false,
                isLit: false,
                lightButton: true,
            },
            {
                id: 1,
                name: "Jardin",
                isWatering: false,
                isLit: false,
                lightButton: true,
            }
        ],
        system: {
            counter: 0
        },
        events: [
            {
                zone: "Potager",
                percent: 33,
            },
        ],
        volume : '',
        simulated: true
    },
    computed: {
        isPumping: function() {
            for (var i=0; i < this.zones.length; i++) {
                if (this.zones[i].isWatering) {
                    return true;
                }
            }

            return false;
        }
    },
    ready: function() {
        this.update();
        setInterval(this.update, 3000);
    },
    methods: {
        update: function() {
            // Get new data from service
            var that = this;
            var param = {
                action: "getInfos"
            };
            $.get("/cgi-bin/Controller.py", param, function(data, status){
                var result = JSON.parse(data);
                console.log(result);
                that.updateUI(result);
            });
        },
        updateUI: function(data) {
            // Update lights
            this.zones[0].isLit = !!+data.light1;
            this.zones[1].isLit = !!+data.light2;
            // Update watering
            this.zones[0].isWatering = !!+data.sprinkler1;
            this.zones[1].isWatering = !!+data.sprinkler2;
            // Update volume counter
            this.system.counter = data.volume;
            // Update progress bars
            $('.progress').progress();
        },
        toggleLight: function(zone) {
            var that = this;
            var param = {
                action: 'set'
            };
            if (zone.id == 0) {
                param.light1 = this.zones[zone.id].isLit ? 0 : 1;
            }
            else if (zone.id == 1) {
                param.light2 = this.zones[zone.id].isLit ? 0 : 1;
            }
            // Post Request to toggle light
            $.get("/cgi-bin/Controller.py", param, function(data, status){
                var result = JSON.parse(data);
                console.log(result);
                // Update UI
                that.updateUI(result);

                // Once light has been switched, turn button back on
                zone.lightButton = true;
            });
            // Deactive light switch
            zone.lightButton = false;
        },
        showModal: function(zone) {
            $('#modal-' + zone.id).modal('show');
        },
        confirmWatering: function(zone, volume) {
            var that = this;
            if (volume > 0) {
                var param = {
                    action: 'set'
                };
                    
                if (zone.id == 0) {
                    param.water1 = volume;
                }
                else if (zone.id == 1) {
                    param.water2 = volume;
                }
                // Set to watering modus
                zone.isWatering = true;
                $.post("/cgi-bin/Controller.py", param, function(data, status){
                    var result = JSON.parse(data);
                    //console.log(result);
                    // Update UI
                    that.updateUI(result);
                });
            }
            // Water those !
            this.volume = '';
        },
    }
});
