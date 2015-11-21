new Vue({
    el: '#app',
    data: {
        zones: [
            { 
                id: 0,
                name: "Potager",
                isWatering: true,
                isLit: true
            },
            { 
                id: 1,
                name: "Jardin",
                isWatering: false,
                isLit: false
            }
        ],
        system: {
            counter: 200
        }
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
    methods: {
        toggleLight: function(zoneId) {
            this.zones[zoneId].isLit = !this.zones[zoneId].isLit;
        },
        showModal: function(zoneId) {
            $('#modal-' + zoneId).modal('show');
        },
        confirmWatering: function(zoneId, volume) {
            this.zones[zoneId].isWatering = !this.zones[zoneId].isWatering;
            // Water those !
        },
    }
});