type UserId = string & { readonly __brand: 'UserId' };

type Result<T> =
  | { ok: true; value: T }
  | { ok: false; error: { code: string; message: string } };

type CreateUser = {
  email: string;
  displayName: string;
};

function parseUserId(value: string): Result<UserId> {
  if (!/^user_[a-zA-Z0-9_-]+$/.test(value)) {
    return { ok: false, error: { code: 'invalid_user_id', message: 'Invalid ID' } };
  }
  return { ok: true, value: value as UserId };
}

async function createUser(input: CreateUser): Promise<Result<{ id: UserId }>> {
  if (!input.email.includes('@')) {
    return { ok: false, error: { code: 'validation_error', message: 'Invalid email' } };
  }
  // Exercise: replace this stub with a repository call.
  return { ok: true, value: { id: 'user_demo' as UserId } };
}

// Exercises:
// 1. Add a discriminated union for domain errors.
// 2. Create a typed pagination result.
// 3. Model API request states with a state-machine union.
// 4. Add runtime validation and explain why TypeScript types alone are insufficient.
// 5. Write tests for each branch and error code.
