from git import Repo
import os

class MyGitPython:

	def __init__(self, repo_path=None):
		"""Initialize a configuration"""
		if not repo_path:
			repo_path = "C:/Users/sangrpatil/Documents/workspace/gitpy/testgitpy"
		self.repo_path = repo_path
		self.repo = self.repo_object()

	def repo_object(self):
		"""validate and create repo Object"""
		try:
			if self.repo_path:
				return Repo(self.repo_path)
		except Exception as e:
			print('Could not load repository at {} :('.format(self.repo_path))
			return None

	def repo_status(self):
		""":return dict of repo dirty status, active branch & untracked file status"""
		try:
			if self.repo:
				return {
					"working_dir": self.repo.working_tree_dir,
					"remote_url": self.repo_remotes(),
					"is_dirty": self.repo.is_dirty(),
					"active_branch": self.repo.active_branch,
					"untracked_files": self.repo.untracked_files
				}
		except Exception as e:
			print('Error found while status check at {}'.format(self.repo_path))
			return {}

	def repo_remotes(self):
		try:
			remotes = list()
			for remote in self.repo.remotes:
				remotes.append({"name": remote.name, "url": remote.url})
			return remotes
		except Exception as e:
			return []

	def commit_details(self, max_commit=5, branch=None):
		try:
			commit_data = list()
			fetched_commits = list(self.repo.iter_commits(branch))[:]
			for idx, commit in enumerate(fetched_commits):
				if idx < max_commit:
					commit_data.append({
						"commit_id": str(commit.hexsha),
						"summary": commit.summary,
						"author_name": commit.author.name,
						"author_email": commit.author.email,
						"datetime": str(commit.authored_datetime),
						"count": commit.count(),
						"size": commit.size
					})
			# to get latest commits on top
			commit_data.reverse()
		except Exception as e:
			print("Error while fetching commits: {}".format(e))
		finally:
			return commit_data

# crete class object and test the functions
git_py = MyGitPython()
print("Repo Details: \n\n", git_py.repo_status())
print("\n\n")
print("Commit Details: \n\n", git_py.commit_details(4, 'master'))


