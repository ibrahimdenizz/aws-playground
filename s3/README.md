# AWS S3

Course link: https://www.youtube.com/watch?v=L3dYocCSU-E

# Notes

- Object Storage
- Cost effective
- Redundancy
- Low latency, high throughput
- easy to host static website
- Can integrate with SNS, SQS, Lambda for powerful event driven applications
- Shift away old data into long term storage for cost reduction.

## Create Bucket

---

### General configuration

- Select Name and Region

### Block Public Access settings

- This block public access with account level as default. You can choose public access options

### Bucket Versioning

- If you enable versioning, when you update object, S3 keeps old objects.
  When you make get request, S3 retrieve latest version of object. Also,
  you can make request with specific version id.

### Tags

- Track cost with tag

## Properties

---

### Server access logging

- Server access logging provides detailed records for the requests that are made to a bucket

### Static website hosting

- You can use Amazon S3 to host a static website. On a static website, individual webpages
  include static content. They might also contain client-side scripts.
- Amazon S3 does not support server-side scripting

### Transfer acceleration

- Fast, easy, and secure transfers of files over long distances between your client and an S3 bucket
- Extra cost! Not cheap.

## Permissions

### Bucket policy

- To give specific permission for specific users with JSON
