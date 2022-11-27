class Tablet:

	MAX_MEMORY = 1024

	MODELS = {
		"lite": {
			"base_storage": 32,
			"memory": 2
		},
		"pro": {
			"base_storage": 64,
			"memory": 3
		},
		"max": {
			"base_storage": 128,
			"memory": 3
		}
	}

	def __init__(self, model):
		model = model.lower().strip()

		if model not in list(self.MODELS.keys()):
			raise ValueError("Model not recognized")

		specs = self.MODELS[model]

		self.model = model
		self._base_storage = specs["base_storage"]
		self._memory = specs["memory"]
		self._added_storage = 0

	def add_storage(self, additional_storage):
		if self._base_storage + additional_storage > self.MAX_MEMORY:
			raise ValueError(f"Device memory cannot exceed {self.MAX_MEMORY}")
		self._added_storage = additional_storage

	@property
	def storage(self):
		return self._base_storage + self._added_storage

	@storage.setter
	def storage(self, memory):
		# figure out the split between base and added
		# check that memory is positive (valid) and it does not exceed max
		# then set added
		additional = memory - self._base_storage

		if additional < 0:
			raise ValueError(f"Device memory cannot be lower than the base memory of {self._base_storage}")

		if memory > self.MAX_MEMORY:
			raise ValueError(f"Device memory cannot exceed maximum of {self.MAX_MEMORY}")

		self._added_storage = additional

	# Make memory and base-storage read-only
	@property
	def memory(self):
		return self._memory

	@property
	def base_storage(self):
		return self._base_storage

	def __repr__(self):
		return f"Tablet(model='{self.model}', base_storage='{self.base_storage}', " \
			   f"added_storage='{self._added_storage}', memory='{self.memory}'"


t1 = Tablet("max")
print(t1)

t1.add_storage(128)
print(t1)

t1.storage = 512
print(t1)

# Tablet("maxlesh")  # not recognized
# t1.memory = 3  # read only
# t1.base_storage = 50  # read-only
