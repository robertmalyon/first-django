# first-django

My first attempt at building a Django app.

To begin with I followed along with a tutorial series by Corey Schaefer, which I found excellent. I managed to replicate, with some slight alterations, the blog app he created. I struggled a great deal with deployment on Linode and after thoroughly watching and following the deployment tutorial twice I still couldn't get it up and running. So I switched to PythonAnywhere, which is specifically geared toward hosting and supporting Python apps. I managed to get it up and running and then I began making changes.

Deployment on PythonAnywhere is supported by GitHub, you can simply clone the repo onto their server and then make a series of fairly straightforward adjustments for server deployment, all the while helped along by their interface. So It's great and I was very pleased to have it up and running in not much time ata ll. And best of all, it's free for their lowest tier of membership, which is more then adequate for this project.

## Thats when it all went wrong...

So at this stage I wanted to use the project as a kind of framework within a framework, upon which to develop my own exciting app. This started off quite well, I pulled the changes down to my local machine, made a load of improvements and then applied those changes server-side. I got pretty confident, made more changes and deployed them and... I broke it.

## Brief outline of the problem

The site appears to be running fine, but when you attempt to login to the admin panel you get an error. Investigation shows that it is trying to access a table that doesn't exist. I think the cause of the problem is something to do with the iterations of making changes to the local and server database structure. It still runs fine locally.

## Things I tried

I made migrations and migrated several times.

I deleted the database and all the migrations individually and then repeated the migration process.

I commented the databse out of the gitignore so that the contents of the local version were replicated on the server.

I tried the 'flush' command, I tried doing a few things in the shell.

I spent a lot of time reading the docs and googling the problem.

## Moving forward

I've halted development. Its better to build the project completely before deploying it, making serious structural changes after deployment can be problematic and might benefit from a complete redeployment.

My plan is this. I could delete the app server-side and just redo the deployment from scratch.

I could start a new project and use the elements I like and am happy with, but approach it from a completely fresh starting point excluding anything that's not specifically relevant or required.

I could continue to learn more, particularly focus on databases, in the hope that I figure out a solution.

I'll do a bit of all three I think. I'll carry on learning, I'll start rebuilding the project bigger and better from scratch AND I'll attempt redeployment just in case it leads to a quick fix that gets something up and running while I work on something more adventurous behind the scenes.
