export type DevUser = {
  id: string;
  name: string;
  email: string;
  role: "support";
};

const DEV_USER_KEY = "aegis-dev-user";

export function signInDevUser(): DevUser {
  const user: DevUser = {
    id: "dev-support-user",
    name: "Support User",
    email: "support.user@aegissoftware.com",
    role: "support",
  };

  window.localStorage.setItem(DEV_USER_KEY, JSON.stringify(user));

  return user;
}

export function getDevUser(): DevUser | null {
  const storedUser = window.localStorage.getItem(DEV_USER_KEY);

  if (!storedUser) {
    return null;
  }

  try {
    return JSON.parse(storedUser) as DevUser;
  } catch {
    window.localStorage.removeItem(DEV_USER_KEY);
    return null;
  }
}

export function signOutDevUser(): void {
  window.localStorage.removeItem(DEV_USER_KEY);
}