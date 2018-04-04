## Django Redirection App
- The core function of this app is to allow redirection from one url to another.
- For instance : if www.abc.com/aniket is a url and is changed to www.abc.com/aniketm then in that case www.abc.com/aniket should redirect user to the new url i.e 301 status code.
- This ensure that the old url if indexed by SEARCH ENGINE doesn't show 404.
- Makes redirection easy

## How to Use
- Plug this app in your `Django` code base. 
- Register it up in Installed Apps as `redirection`
- In MIDDLEWARE section define `redirection.middleware.RedirectionBasedOnSlug`
- That's about it.

### PR's are welcome

