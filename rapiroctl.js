/* Extension demonstrating a blocking command block */
/* Sayamindu Dasgupta <sayamindu@media.mit.edu>, May 2014 */

/* file:///home/pi/Scratch/Extensions/rapiroctl.js */

new (function() {
    var ext = this;

    // Cleanup function when the extension is unloaded
    ext._shutdown = function() {};

    // Status reporting code
    // Use this to report missing hardware, plugin or unsupported browser
    ext._getStatus = function() {
        return {status: 2, msg: 'Ready'};
    };

    // Functions for block with type 'w' will get a callback function as the 
    // final argument. This should be called to indicate that the block can
    // stop waiting.
    ext.rapiro_command = function(command, callback) {
        $.ajax({
              url: 'http://rapiropi/' + command,
              dataType: 'html',
              success: function(data, textStatus) {
                  callback();
              },
              error: function(xhr, textStatus, errorThrown){
                  alert('Error! ' + textStatus + ' ' + errorThrown);
                  callback();
              }
        });
    };
    ext.rapiro_command_M0 = function(callback) {
        ext.rapiro_command("M0", callback); 
    };
    ext.rapiro_command_M1 = function(callback) {
        ext.rapiro_command("M1", callback); 
    };
    ext.rapiro_command_M2 = function(callback) {
        ext.rapiro_command("M2", callback); 
    };
    ext.rapiro_command_M3 = function(callback) {
        ext.rapiro_command("M3", callback); 
    };
    ext.rapiro_command_M4 = function(callback) {
        ext.rapiro_command("M4", callback); 
    };
    ext.rapiro_command_M5 = function(callback) {
        ext.rapiro_command("M5", callback); 
    };
    ext.rapiro_command_M6 = function(callback) {
        ext.rapiro_command("M6", callback); 
    };
    ext.rapiro_command_M7 = function(callback) {
        ext.rapiro_command("M7", callback); 
    };
    ext.rapiro_command_M8 = function(callback) {
        ext.rapiro_command("M8", callback); 
    };
    ext.rapiro_command_M9 = function(callback) {
        ext.rapiro_command("M9", callback); 
    };
    ext.rapiro_command_LOW = function(callback) {
        ext.rapiro_command("LOW", callback); 
    };
    ext.rapiro_command_PLAY = function(name, callback) {
        cmd = "PLAY?name=" + name;
        ext.rapiro_command(cmd, callback); 
    };

    // Block and block menu descriptions
    var descriptor = {
        blocks: [
            ["w", "停止する", "rapiro_command_M0"],
            ["w", "前進する", "rapiro_command_M1"],
            ["w", "後退する", "rapiro_command_M2"],
            ["w", "右に曲がる", "rapiro_command_M3"],
            ["w", "左に曲がる", "rapiro_command_M4"],
            ["w", "両手を振る", "rapiro_command_M5"],
            ["w", "右手を振る", "rapiro_command_M6"],
            ["w", "両手を握る", "rapiro_command_M7"],
            ["w", "左手を振る", "rapiro_command_M8"],
            ["w", "右手を伸ばす", "rapiro_command_M9"],
            ["w", "モータを止める", "rapiro_command_LOW"],
            ["w", "%s を再生する", "rapiro_command_PLAY"],
        ],
        "menus": {}
    };

    // Register the extension
    ScratchExtensions.register('RAPIRO control', descriptor, ext);
})();