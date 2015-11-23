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
            $.get("/autarco/update", function(data, status){
                alert("Data: " + data + "\nStatus: " + status);
                this.updateUI(data);
            });
        },
        updateUI: function(data) {
            // Update local data
            this.zones = data.zones;
            this.system = data.system;
            this.events = data.events;
            // Update progress bars
            $('.progress').progress();
        },
        toggleLight: function(zone) {
            var data = {
                zoneId: zone.id,
            };
            // Post Request to toggle light
            $.post("/autarco/light", data, function(data, status){
                alert("Data: " + data + "\nStatus: " + status);
                // Update UI
                this.updateUI(data);

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