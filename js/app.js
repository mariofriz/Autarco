new Vue({
    el: '#app',
    data: {
        zones: [
            {
                id: 0,
                name: "Potager",
                isWatering: true,
                isLit: true,
                wateringButton: true,
                lightButton: true,
            },
            {
                id: 1,
                name: "Jardin",
                isWatering: false,
                isLit: false,
                wateringButton: true,
                lightButton: true,
            }
        ],
        system: {
            counter: 200
        },
        events: [
            {
                zone: "Potager",
                percent: 33,
            },
        ],
        volume : ''
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
            $.get("/cgi-bin/Controller.py?action=getInfos", function(data, status){
                var result = JSON.parse(data);
                console.log(result);
                that.updateUI(result);
            });
        },
        updateUI: function(data) {
            // Update lights
            console.log(data.light1);
            this.zones[0].isLit = !!+data.light1;
            console.log(this.zones[0].isLit);
            this.zones[1].isLit = !!+data.light2;
            // Update watering
            this.zones[0].isWatering = !!+data.sprinkler1;
            this.zones[1].isWatering = !!+data.sprinkler2;
            // Update volume counter
            // TODO
            // Update progress bars
            $('.progress').progress();
        },
        toggleLight: function(zone) {
            var data = {};
            if (zone.id == 0) {
                data.light1 = !this.zones[zone.id].isLit;
            }
            else if (zone.id == 1) {
                data.light2 = !this.zones[zone.id].isLit;
            }
            // Post Request to toggle light
            $.get("/cgi-bin/Controller.py?action=set"+, data, function(data, status){
                var result = JSON.parse(data);
                console.log(result);
                // Update UI
                // this.updateUI(result);

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
            if (volume > 0) {
                var data = {
                    zoneId: zone.id,
                    volume: volume
                };
                $.post("/autarco/water", data, function(data, status){
                    alert("Data: " + data + "\nStatus: " + status);
                    // Update UI
                    this.updateUI(data);

                    // Once event is registered reactivate button
                    zone.wateringButton = true;
                });
                // Deactivate watering button
                zone.wateringButton = false;
            }
            // Water those !
            this.volume = '';
        },
    }
});
