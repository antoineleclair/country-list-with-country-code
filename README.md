Country List
============

During a client project using Paypal DirectPayment API, I had to make a `<select>` with all the countries with their country code as the value. For example:

    <option value="US">United States</option>
    <option value="CA">Canada</option>

Paypal already gives this list https://www.paypalobjects.com/en_US/ebook/PP_NVPAPI_DeveloperGuide/countrycodes_new.html.

Problem is that it's only in English and all in caps. What I needed is a French version and an English version, not in caps.

[Geonames.org](http://geonames.org/) just happens to have what I needed. This script is what I coded to generate what I needed.

Hope it's useful to someone else.
