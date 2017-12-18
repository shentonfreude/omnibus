=================
 README: OmniBus
=================

I want to create an app that is as convenient as the Android app by
Transit App, Inc.  Their app works on Android and iOS but I want one
that I can invoke from my Amazon Alexa device. I'd also like to use
this as a sample project to for an Angular-based webapp. All
processing should be done using serverless tech in AWS.

Alexa
=====

It would be nice to shout at our Echo Dot and find when the next bus
is. We've got several lines and stops nearby; we might want to hear
all of them:

Q: Alexa, ask Omnibus next arrival.

A: ART 55 to Rosslyn in 3 minutes; ART 55 to East Falls Church in 2 minutes.
   WMATA 3Y to Foggy Bottom in 8 minutes; ...

Or we should be able to ask for specific routes and/or directions:

Q: Alexa, ask Omnibus ART 55

A: ART 55 to Rosslyn in 3 minutes; ART 55 to East Falls Church in 2 minutes.

or:

Q: Alexa, ask Omnibus ART 55 to East Falls Church

A: ART 55 to East Falls Church in 2 minutes.

Angular Web App
===============

I'm trying to learn Angular and want to build a progressive web app
(PWA). Once I've figured out how to get and parse data for the Alexa
skill, I'd like to use the same logic to back an web-based PWA.

Serverless Back-end
===================

I've been doing a bunch of work with AWS Lambda and the Serverless
Framework. This seems a great use for that tech. It also seems how
Alexa skills are intended to be implemented.

