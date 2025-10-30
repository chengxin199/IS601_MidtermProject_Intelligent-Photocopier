# Docker Containerization Best Practices: Practical Exercises

## Exercise 1: Efficient Dockerfile Configurations

### Objective:
Create an efficient Dockerfile for a simple Node.js application.

### Instructions:
1. **Set Up Your Project**:
   - Create a new directory called `node-app` and navigate into it.
   - Inside this directory, create a simple Node.js application. You can use the following files:
     - `package.json`: 
       ```json
       {
         "name": "node-app",
         "version": "1.0.0",
         "main": "index.js",
         "scripts": {
           "start": "node index.js"
         },
         "dependencies": {
           "express": "^4.17.1"
         }
       }
       ```
     - `index.js`: 
       ```javascript
       const express = require('express');
       const app = express();
       const port = process.env.PORT || 3000;

       app.get('/', (req, res) => {
         res.send('Hello World!');
       });

       app.listen(port, () => {
         console.log(`App listening at http://localhost:${port}`);
       });
       ```

2. **Create Your Dockerfile**:
   - In the `node-app` directory, create a file named `Dockerfile` and write the following content:
     ```dockerfile
     FROM node:14

     WORKDIR /usr/src/app

     COPY package*.json ./
     RUN npm install --production

     COPY . .

     EXPOSE 3000
     CMD ["npm", "start"]
     ```

3. **Build Your Docker Image**:
   - Run the following command in the terminal:
     ```bash
     docker build -t node-app .
     ```

4. **Run Your Container**:
   - Use the following command to run your container:
     ```bash
     docker run -d -p 3000:3000 node-app
     ```

### Acceptance Criteria:
- A Dockerfile that follows best practices for a Node.js application.
- The application should be accessible at `http://localhost:3000` and return "Hello World!".
  
### Hints:
- Ensure you are using the appropriate base image for your application.
- Pay attention to the order of commands in your Dockerfile to optimize caching.

---

## Exercise 2: Implementing Multi-Stage Builds

### Objective:
Refactor the Dockerfile from Exercise 1 to use multi-stage builds.

### Instructions:
1. **Modify the Dockerfile**:
   - Update your `Dockerfile` to include a build stage. The new Dockerfile should look like this:
     ```dockerfile
     # Stage 1: Build the application
     FROM node:14 AS build

     WORKDIR /usr/src/app
     COPY package*.json ./
     RUN npm install

     COPY . .
     RUN npm run build

     # Stage 2: Run the application
     FROM node:14 AS production

     WORKDIR /usr/src/app
     COPY --from=build /usr/src/app .

     RUN npm install --production

     EXPOSE 3000
     CMD ["npm", "start"]
     ```

2. **Rebuild Your Docker Image**:
   - Run the build command again:
     ```bash
     docker build -t node-app .
     ```

3. **Run Your Container**:
   - Start your container with:
     ```bash
     docker run -d -p 3000:3000 node-app
     ```

### Acceptance Criteria:
- The application should be running in a production-ready container.
- The image size should be smaller due to the use of multi-stage builds.

### Hints:
- Ensure that your application does not try to run build commands in the production stage.
- Look into how to build assets if your application requires it (e.g., `npm run build`).

---

## Exercise 3: Applying Container Security Best Practices

### Objective:
Secure your Docker image by implementing best practices.

### Instructions:
1. **Modify the Dockerfile for Security**:
   - Update your Dockerfile to include the following security practices:
     - Use a non-root user.
     - Reduce the number of layers.
     - Set the `NODE_ENV` to `production`.

   Revised Dockerfile:
   ```dockerfile
   FROM node:14 AS build

   WORKDIR /usr/src/app
   COPY package*.json ./
   RUN npm install

   COPY . .

   FROM node:14 AS production
   ENV NODE_ENV=production

   WORKDIR /usr/src/app
   RUN addgroup --system appgroup && adduser --system appuser --ingroup appgroup
   USER appuser

   COPY --from=build /usr/src/app .

   RUN npm install --production

   EXPOSE 3000
   CMD ["npm", "start"]
   ```

2. **Rebuild Your Docker Image**:
   - Use the command:
     ```bash
     docker build -t node-app .
     ```

3. **Run Your Container**:
   - Start your container:
     ```bash
     docker run -d -p 3000:3000 node-app
     ```

### Acceptance Criteria:
- The application must run under a non-root user.
- The environment variable `NODE_ENV` should be set to `production`.

### Hints:
- Ensure you have the `adduser` and `addgroup` commands in your Dockerfile, as some base images may not have them installed by default.

---

## Exercise 4: Optimizing Image Size and Build Times

### Objective:
Optimize the Docker image for faster builds and smaller size.

### Instructions:
1. **Optimize Dockerfile**:
   - Modify your Dockerfile to include the following optimizations:
     - Combine commands where possible to reduce layers.
     - Avoid unnecessary files in the image (e.g., use `.dockerignore`).

   Example `.dockerignore`:
   ```
   node_modules
   npm-debug.log
   ```

   Update your Dockerfile to combine layers:
   ```dockerfile
   FROM node:14 AS build

   WORKDIR /usr/src/app
   COPY package*.json ./
   RUN npm install && npm cache clean --force

   COPY . .

   FROM node:14 AS production
   ENV NODE_ENV=production

   WORKDIR /usr/src/app
   RUN addgroup --system appgroup && adduser --system appuser --ingroup appgroup
   USER appuser

   COPY --from=build /usr/src/app .

   RUN npm install --production && npm cache clean --force

   EXPOSE 3000
   CMD ["npm", "start"]
   ```

2. **Rebuild Your Docker Image**:
   - Run:
     ```bash
     docker build -t node-app .
     ```

3. **Run Your Container**:
   - Start your container:
     ```bash
     docker run -d -p 3000:3000 node-app
     ```

### Acceptance Criteria:
- The image size should be reduced compared to previous builds.
- The application must still function correctly.

### Hints:
- Use `docker image history node-app` to inspect the size of each layer and identify large layers.
- Be mindful of what files you copy into the image. Use `.dockerignore` effectively.

---

## Exercise 5: Managing Container Orchestration Basics

### Objective:
Deploy your application using Docker Compose for orchestration.

### Instructions:
1. **Create a Docker Compose File**:
   - In the `node-app` directory, create a file named `docker-compose.yml`:
     ```yaml
     version: '3.8'
     services:
       app:
         build: .
         ports:
           - "3000:3000"
         environment:
           NODE_ENV: production
         user: appuser
     ```

2. **Run Your Application with Docker Compose**:
   - Use the following command to start your application:
     ```bash
     docker-compose up --build
     ```

3. **Access Your Application**:
   - Navigate to `http://localhost:3000` to ensure it is running.

### Acceptance Criteria:
- The application must run successfully using Docker Compose.
- Ensure that the application is still accessible at `http://localhost:3000`.

### Hints:
- Use `docker-compose logs` to troubleshoot any issues with the application startup.
- Remember to stop your services with `docker-compose down` when you’re done.

---

These exercises are designed to deepen your understanding of Docker best practices while providing practical, hands-on experience with containerization. Happy coding!