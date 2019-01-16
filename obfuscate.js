#!/usr/bin/node

const process = require('process');

const jsKey = process.argv[2];

const JavaScriptObfuscator = require('javascript-obfuscator');

const obfuscationResult = JavaScriptObfuscator.obfuscate(
    `
        (function(){
            if (window.parent.location.host != "127.0.0.1:5000") {
                return;
            }
        
            if (window.location.host != "127.0.0.1:5000") {
                return;
            }
            
            window.location.href = "/js-check/` + jsKey + `";
        })();
    `,
    {
        compact: false,
        controlFlowFlattening: true,
        selfDefending: true,
        deadCodeInjection: true,
        stringArray: true,
        rotateStringArray: true,
        stringArrayEncoding: 'rc4'
    }
);

console.log(obfuscationResult.getObfuscatedCode());
