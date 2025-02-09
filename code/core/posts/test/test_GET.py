from django.test import TestCase
from django.contrib.auth import get_user_model
from graphene.test import Client
from posts.models import Post
from posts.apis.grapql.schema import posts_schema
from globals.test_objects import create_token_headers

User = get_user_model()

class TestPostSchemaTests(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username="testuser", password="testpass")
        
        # Create a test post
        self.post = Post.objects.create(
            body="This is a test post.",
            owner=self.user
        )
        
        # Initialize the GraphQL client
        self.client = Client(posts_schema)

    def test_resolve_user_timeline(self):
        # Simulate authentication by passing the user in the context
        query = """
        query {
            userTimeline {
                id
                body
                owner {
                    id
                    username
                }
            }
        }
        """
        executed = self.client.execute(query, context_value={"headers": create_token_headers(self.user) })
        
        self.assertNotIn("errors", executed)
        self.assertEqual(len(executed["data"]["userTimeline"]), 0)

    def test_resolve_get_post_by_id(self):
        query = """
        query GetPostById($postId: Int!) {
            getPostById(postId: $postId) {
                id
                body
                owner {
                    username
                }
            }
        }
        """
        variables = {"postId": self.post.id}
        executed = self.client.execute(query, variables=variables)
        
        # Assert no errors
        self.assertNotIn("errors", executed)
        
        # Assert the response matches the test post
        self.assertEqual(executed["data"]["getPostById"]["id"], str(self.post.id))
        self.assertEqual(executed["data"]["getPostById"]["body"], self.post.body)
        self.assertEqual(executed["data"]["getPostById"]["owner"]["username"], self.user.username)

    def test_resolve_get_post_by_id_not_found(self):
        query = """
        query GetPostById($postId: Int!) {
            getPostById(postId: $postId) {
                id
                body
            }
        }
        """
        variables = {"postId": 999}  # Non-existent post ID
        executed = self.client.execute(query, variables=variables)
        
        # Assert errors
        self.assertIn("errors", executed)
        self.assertEqual(executed["errors"][0]["message"], "Post not found")

    def test_resolve_get_post_by_owner_username(self):
        query = """
        query GetPostByOwnerUsername($postOwnerUsername: String!) {
            getPostByOwnerUsername(postOwnerUsername: $postOwnerUsername) {
                id
                body
                owner {
                    username
                }
            }
        }
        """
        variables = {"postOwnerUsername": self.user.username}
        executed = self.client.execute(query, variables=variables)
        
        # Assert no errors
        self.assertNotIn("errors", executed)
        
        # Assert the response matches the test post
        self.assertEqual(len(executed["data"]["getPostByOwnerUsername"]), 1)
        self.assertEqual(executed["data"]["getPostByOwnerUsername"][0]["id"], str(self.post.id))
        self.assertEqual(executed["data"]["getPostByOwnerUsername"][0]["body"], self.post.body)
        self.assertEqual(executed["data"]["getPostByOwnerUsername"][0]["owner"]["username"], self.user.username)

    def test_resolve_get_post_by_owner_username_not_found(self):
        query = """
        query GetPostByOwnerUsername($postOwnerUsername: String!) {
            getPostByOwnerUsername(postOwnerUsername: $postOwnerUsername) {
                id
                body
            }
        }
        """
        variables = {"postOwnerUsername": "nonexistentuser"}  # Non-existent username
        executed = self.client.execute(query, variables=variables)
        
        # Assert no errors
        self.assertNotIn("errors", executed)
        
        # Assert the response is empty
        self.assertEqual(len(executed["data"]["getPostByOwnerUsername"]), 0)