/* PLEASE DO NOT COPY AND PASTE THIS CODE. */(function(){var w=window,C='___grecaptcha_cfg',cfg=w[C]=w[C]||{},N='grecaptcha';var gr=w[N]=w[N]||{};gr.ready=gr.ready||function(f){(cfg['fns']=cfg['fns']||[]).push(f);};w['__recaptcha_api']='https://www.google.com/recaptcha/api2/';(cfg['render']=cfg['render']||[]).push('explicit');(cfg['onload']=cfg['onload']||[]).push('recaptchaCallbackba515a91ef1045658c49482043c590cc');w['__google_recaptcha_client']=true;var d=document,po=d.createElement('script');po.type='text/javascript';po.async=true;var s='https://www.gstatic.com/recaptcha/releases/vm_YDiq1BiI3a8zfbIPZjtF2/recaptcha__en.js',tt=w.trustedTypes,cp=tt&&tt.createPolicy,cp=cp&&cp.bind(tt); po.src=cp?cp('recaptcha', {createScriptURL:function(_){return s;}}).createScriptURL(''):s;po.crossOrigin='anonymous';po.integrity='sha384-jmuBB3ajBz67HkD9EOwlByuyyxCYut7RyJGCbt+luJzVIFeqE/GGKvIVjUTdjP4o';var e=d.querySelector('script[nonce]'),n=e&&(e['nonce']||e.getAttribute('nonce'));if(n){po.setAttribute('nonce',n);}var s=d.getElementsByTagName('script')[0];s.parentNode.insertBefore(po, s);})();