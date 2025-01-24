## For creating EC2 AMI please add tag for that EC2. Key: Project, Value <ProjectName>
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. From the navigation bar, select the Region where the resource to tag is located. For more information, see Resource locations.
3. In the navigation pane, select Instances.
4. Select the EC2 and choose the Tags tab.
5. Choose Manage tags, and then choose Add new tag. Enter the key and value for the tag. Choose Save

## If the project has scaling you need to add same tag for Launch Templates and Auto Scaling groups too:
### Launch Template  
1. Open the Launch Template section.
2. Select the project Launch Template
3. In the Launch template details pane, select Template tags
4. Choose Manage tags, and then choose Add new tag. Enter the key (Project) and value(<ProjectName>) for the tag. Choose Save
### Auto Scaling Groups
1. Open the Auto Scaling Groups section.
2. Select the project Auto Scaling Group
3. In the Auto Scaling Group details pane, select tags
4. Choose Manage tags, and then choose Add new tag. Enter the key (Project) and value(<ProjectName>) for the tag. Choose Save

## After image creation old images and snapshots are deleted if the tags exists for those images and snapshots 

## The default value for lambda function execution time is 3 seconds, but you can adjust this in increments of 1 second up to a maximum value of 15 minutes.
### To change the timeout of a function
1. Open the Functions page of the Lambda console.
2. Choose a function.
3. On the function configuration page, on the General configuration pane, choose Edit.
4. For Timeout, set a value from 1 second to 15 minutes.
5. Choose Save.

## Asynchronous invocation – Lambda retries function errors twice
#### The LambdaInvokeOtherFunction call another (LambdaTakeEC2AmiAndUpdateLT). For disable retries LambdaTakeEC2AmiAndUpdateLT after error 

1. Open the Functions page of the Lambda console.
2. Choose a function.
3. On the function configuration page, on the Asynchronous invocation pane, choose Edit.
4. For retry attempts, set a value 0.
5. Choose Save.