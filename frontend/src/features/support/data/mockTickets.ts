export type TicketStatus =
  | "Open"
  | "In progress"
  | "Resolved";

export type SupportTicket = {
  id: string;
  subject: string;
  category: string;
  status: TicketStatus;
  createdAt: string;
  updatedAt: string;
};

export const mockTickets: SupportTicket[] = [
  {
    id: "TKT-1042",
    subject: "Unable to access secure upload request",
    category: "Access",
    status: "Open",
    createdAt: "2026-06-18",
    updatedAt: "2026-06-21",
  },
  {
    id: "TKT-1038",
    subject: "File upload stopped before completion",
    category: "File upload",
    status: "In progress",
    createdAt: "2026-06-14",
    updatedAt: "2026-06-20",
  },
  {
    id: "TKT-1029",
    subject: "Question about request expiration",
    category: "Expiration",
    status: "Resolved",
    createdAt: "2026-06-08",
    updatedAt: "2026-06-10",
  },
];