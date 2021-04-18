# A Simple Inclusive Avatar Generator

This is a really simple avatar generator I created for my last project. It's been incredibly helpful for all my new projects too so I decided to tidy it up a bit and make it available for anyone to use.

You create images with - [avatar.windsor.io/{anything}](https://avatar.windsor.io/{anything}).

`{anything}` can be anything, like an email address, user id, full name, url, ssn, etc.

For a given path, you'll always get back the same image, which is what makes this a great default avatar to use on your site.

I often use [avatar.windsor.io/{user.email}](avatar.windsor.io/{user.email}) as a default for most of my apps so the avatar for that user is consistent across any product of mine they use (and now your products too)!

## To deploy this yourself

### Setup

1. Clone repo
2. `pip install -r requirements.txt`
3. `./build-robohash.sh`

### If you want to make your own changes to the avatar images

1. Change the assets in `robohash-src/robohash/sets`
2. `./build-robohash.sh`

### To deploy

#### With Vercel

1. Modify the alias field in `now.json` to wherever you want to deploy it to
2. `vercel --prod`

#### On a different deployment platform

1. Simulate the vercel behaviour with `rewrites` in now.json and loading/serving the api routes in `api`.
  You can do this with writing your own server, or using AWS API Gateway or cloudflare workers or anything else you'd like :)
2. Deploy, both the server code above, and the static resources (index.html and robots.txt)