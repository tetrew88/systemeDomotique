var socket = io.connect("http://192.168.0.16:5000/HomeAutomationServer", { transports: ['websocket', 'polling', 'flashsocket'] })

function pause(ms)
{
  return new Promise(resolve => setTimeout(resolve, ms));
}