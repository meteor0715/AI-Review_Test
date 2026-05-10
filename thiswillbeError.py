# Dry run — inspect the request without a real token
from unittest.mock import patch, MagicMock

with patch("github_client.status_updater.httpx.post") as mock_post:
    mock_post.return_value = MagicMock(status_code=201, json=lambda: {})
    from github_client.status_updater import set_commit_status
    set_commit_status("fake", "owner/repo", "abc123", "pending", "AI Review starting…")
    set_commit_status("fake", "owner/repo", "abc123", "success", "AI Review complete — 0 HIGH issues")
    print(f"✅ set_commit_status called {mock_post.call_count} times")
    for call in mock_post.call_args_list:
        print("  State:", call.kwargs["json"]["state"],
              "| Description:", call.kwargs["json"]["description"])