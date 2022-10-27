# Software Design and Analysis Website [![Netlify Status](https://api.netlify.com/api/v1/badges/3fbbab05-cf15-4ac2-854f-f2ac1ed81672/deploy-status)](https://app.netlify.com/sites/sdlab/deploys)

## Environment setup

1. Install the static site generator, [Hugo](https://gohugo.io/).  
   We confirmed Hugo v0.84.1 works.
   Extended version (with Sass/SCSS support) is needed.
   Depending on the platform and version used, the extended version may not be installed by default, so please make sure.
2. Please clone this repository.  
    ```
    git clone https://github.com/sdlab-naist/website
    ```
3. Launch a server for delopment.  
Open `localhost:1313` in your browser to see the generated website.
    ```
    hugo server
    ```

For more information on how to set up and create pages, please refer to the [documentation](https://wowchemy.com/docs/) of the Wowchemy theme.

## Workflow
We use Github to manage the web contents in a PullRequest-driven manner.
Before starting editing, you must create a branch, push it to the Github repository, and then issue a PullRequest.
Every PullRequest must be reviewed by at least one person before being merged into the master branch.
The following is an example of a typical workflow.

1. Update your local master branch to the latest version.  
```
git checkout master
git pull
```

2. Create a branch for working.  
Replace `name-of-branch` with an appropriate name to discribe your edit.
```
git checkout -b name-of-branch
```

3. Do some editing.  
If you are running `hugo server`, you can open `localhost:1313` in your browser and see your edits.

4. Please commit.
```
git add .
git commit -m "comments"
```

5. Push your commit.  
`name-of-branch` must be the same as your current working branch.
```
git push origin name-of-branch
```

6. Access to Github and issue a PullRequest to request that your `name-of-branch` be merged into the `master` branch.  
Once the review is complete and the branch is merged into the master, it will be published on our website.

7. After updating the local master branch, you may delete the merged working branch.
```
git checkout master
git pull
git branch -d name-of-branch
```

The followings are examples of how to add each content.

## Add a user

1. Execute the following command to create a user directory.  
    Replace `firstname-lastname` with your name.
    ```
    $ hugo new --kind authors content/en/authors/firstname-lastname
    ```
    A directory named `content/en/authors/firstname-lastname` will be created.

2. Edit `_index.md` in the generated directory and fill the name, profile and other info. The following items must be specified:
    - `title`: Full name (with a space between first and last name)
    - `role`: should be `Professor`, `Master's Student` or `Doctoral Student`
    - `user_groups`: Specify any of the following: `Staff` for faculty, `Student` for students, or `Past Student` for graduates.
    - `weight`: The template does not include this field, but please add this after the `user_groups` field.
    If you are a current student, enter the year and month of admission as a number, e.g. `202004`. If you are a graduate, enter the year and month of graduation.

3. Replace `avatar.jpg` in the directory with your own photo.  
    The aspect ratio should be square and the size should be approximately 500 pixels square.
    If both the English and Japanese pages are created separately, the image should be included only in the directory of the Japanese version. The same image will be reused.

4. Create a Japanese version of the page.  
    If you would like to just reuse the English version of the page as is, create a symbolic link.
    ```
    cd content/ja/authors/
    ln -s ../../en/authors/firstname-lastname
    ```
    If you would like to create a Japanese version of the page, execute the following command to create a directory.
    ```
    $ hugo new --kind authors content/ja/authors/firstname-lastname
    ```
    Then, edit the template as described above.

The member list page is automatically updated.

## Add a blog post

1. Execute the following command to create a post directory.
    ```
    $ hugo new  --kind post content/en/post/title-of-your-blog-post
    ```
    A directory named `content/en/post/title-of-your-blog-post` will be created.

2. Edit `index.md` in the generated directory and write the post.  
    The following items must be specified.
    - `title`: Title of the post.
    - `authors`: Author of the post (in the form `firstname-lastname`, specified when the user was created)

3. If you have a photo or an image to attach to the post, save it in the same directory with the file name `featured.jpg/png`.  
The image will be automatically used as an eye-catching image.
If you would like to attach multiple photos or images, save them in the same directory, and refer to them from the post using the figure shortcode.

4. Create a Japanese version of the post.  
    If you would like to create a Japanese version of the post, execute the following command to create a directory.
    ```
    $ hugo new  --kind post content/ja/post/title-of-your-blog-post
    ```
    Then, edit the post.


## Add a research project

1. Execute the following command to create a directory for your research project.
    ```
    $ hugo new --kind project content/en/project/title-of-your-project
    ```
    A directory named `content/en/project/title-of-your-project` will be created.

2. Edit `index.md` in the generated directory and discribe the project.  
    The following items must be specified.
    - `title`: Title of the post.
    - `authors`: Author of the post (in the form `firstname-lastname`, specified when the user was created)
    - `tags`: Select at least one tag from the major category tags ("Software Process", "Repository Mining", "Software Analytics", "Cloud", "HPC"), and specify additional appropriate tags as needed. (e.g.: `tags: ["Cloud", "SDN"]`)

3. If you have a photo or an image to attach to the post, save it in the same directory with the file name `featured.jpg/png`.  
The image will be automatically used as an eye-catching image.
If you would like to attach multiple photos or images, save them in the same directory, and refer to them from the post using the figure shortcode.

4. Create a Japanese version of the project.  
    If you would like to just reuse the English version of the page as is, create a symbolic link.
    ```
    cd content/ja/project/
    ln -s ../../en/project/title-of-your-project
    ```
    If you would like to create a Japanese version of the page, execute the following command to create a directory.
    ```
    $ hugo new --kind project content/ja/project/title-of-your-project
    ```


## Add photos to the Photo Gallery

Add photo files into the directory, `content/ja/gallery/album`
