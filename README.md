## Getting started

My account uses the FB oAuth feature so the login flow is a little more complicated.
Reversing the login flow with a normal email account is probably more straight forward.

Until auth is reversed, follow these directions to intercept traffic on your mobile device:
https://medium.com/testvagrant/intercept-ios-android-network-calls-using-mitmproxy-4d3c94831f62

Once you login to Touchtunes any request you send should have a `Authorization: Bearer $TOKEN` in the header. Pass that string when you create the TouchTunes API object and everything should work properly.
